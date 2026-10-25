"""Markdown units: paragraphs, list items, table rows, headings — shared by lint, claims and apply-factcheck."""
import re

from common import LINK_RE

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LIST_RE = re.compile(r"^(\s{0,3})([-*+]|\d{1,3}[.)])\s+(.*)$")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
INCLUDE_LINE = "{% include opportunities-top5.html %}"
FOOTER_PREFIXES = ("sources", "couldn't verify", "could not verify", "verification", "dropped", "what was dropped")
EXEMPT_PREFIXES = ("**my read:**", "**my read**:", "*my read:*", "_my read:_", "my read:", "**my take:**",
                   "*nothing verifiable", "_nothing verifiable", "nothing verifiable", "*quiet week", "_quiet week",
                   "quiet week")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"“(\[*_])")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def is_footer_heading(text):
    t = text.strip().lstrip("#").strip().lower()
    return t.startswith(FOOTER_PREFIXES)


def is_exempt(text):
    return text.strip().lower().startswith(EXEMPT_PREFIXES)


def normalize_paragraphs(body):
    """Join hard-wrapped lines of plain paragraphs and list items into single lines (rendering is unchanged)."""
    out = []
    lines = body.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    in_fence = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        if in_fence or not line.strip() or HEADING_RE.match(line) or line.lstrip().startswith("|") \
                or line.strip() == INCLUDE_LINE or re.match(r"^\s*(---|\*\*\*|___)\s*$", line) \
                or line.lstrip().startswith(">"):
            out.append(line)
            i += 1
            continue
        buf = [line.rstrip()]
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if not nxt.strip() or HEADING_RE.match(nxt) or LIST_RE.match(nxt) or nxt.lstrip().startswith("|") \
                    or FENCE_RE.match(nxt) or nxt.strip() == INCLUDE_LINE or nxt.lstrip().startswith(">") \
                    or re.match(r"^\s*(---|\*\*\*|___)\s*$", nxt):
                break
            buf.append(nxt.strip())
            j += 1
        out.append(" ".join(buf))
        i = j
    return "\n".join(out)


def units(body):
    """Split a (normalized) body into units. Each: dict(line, kind, text, section, footer, exempt)."""
    res = []
    section = ""
    footer = False
    in_fence = False
    table_started = False
    for n, line in enumerate(body.split("\n"), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            res.append({"line": n, "kind": "code", "text": line, "section": section, "footer": footer, "exempt": True})
            continue
        if in_fence:
            res.append({"line": n, "kind": "code", "text": line, "section": section, "footer": footer, "exempt": True})
            continue
        if not line.strip():
            table_started = False
            res.append({"line": n, "kind": "blank", "text": "", "section": section, "footer": footer, "exempt": True})
            continue
        m = HEADING_RE.match(line)
        if m:
            section = m.group(2).strip()
            footer = is_footer_heading(section)
            res.append({"line": n, "kind": "heading", "text": section, "level": len(m.group(1)), "section": section,
                        "footer": footer, "exempt": True})
            table_started = False
            continue
        if line.strip() == INCLUDE_LINE:
            res.append({"line": n, "kind": "include", "text": line.strip(), "section": section, "footer": footer,
                        "exempt": True})
            continue
        if re.match(r"^\s*(---|\*\*\*|___)\s*$", line):
            res.append({"line": n, "kind": "hr", "text": line, "section": section, "footer": footer, "exempt": True})
            continue
        if line.lstrip().startswith("|"):
            if TABLE_SEP_RE.match(line):
                res.append({"line": n, "kind": "row-sep", "text": line, "section": section, "footer": footer,
                            "exempt": True})
                continue
            kind = "row-header" if not table_started else "row"
            table_started = True
            res.append({"line": n, "kind": kind, "text": line.strip(), "section": section, "footer": footer,
                        "exempt": kind == "row-header"})
            continue
        if line.lstrip().startswith(">"):
            txt = line.lstrip()[1:].strip()
            res.append({"line": n, "kind": "quote", "text": txt, "section": section, "footer": footer,
                        "exempt": is_exempt(txt)})
            continue
        lm = LIST_RE.match(line)
        if lm:
            txt = lm.group(3).strip()
            res.append({"line": n, "kind": "li", "text": txt, "section": section, "footer": footer,
                        "exempt": is_exempt(txt)})
            continue
        txt = line.strip()
        res.append({"line": n, "kind": "para", "text": txt, "section": section, "footer": footer,
                    "exempt": is_exempt(txt)})
    return res


def sentences(text):
    parts = [s.strip() for s in SENT_SPLIT.split(text or "")]
    return [s for s in parts if s]


def links_in(text):
    return [(m.group(1), m.group(2)) for m in LINK_RE.finditer(text or "")]


def content_units(all_units):
    """Units that carry prose subject to the rules: not footer, not headings/blank/code/hr/include/separators."""
    return [u for u in all_units if not u["footer"] and u["kind"] in ("para", "li", "row", "quote")]
