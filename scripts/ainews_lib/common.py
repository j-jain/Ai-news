"""Shared helpers: paths, JSON, dates, URL canonicalisation, text normalisation, front matter, git/gh."""
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.parse

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # pragma: no cover
    pass

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SITE_URL = "https://j-jain.github.io/Ai-news"
REPO_SLUG = "j-jain/Ai-news"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
EDITIONS = ("india", "world")
INDIA_BEATS = ("india-labs-policy", "india-money-adoption", "opportunities")


def p(*parts):
    return os.path.join(ROOT, *parts)


def rel(path):
    try:
        return os.path.relpath(path, ROOT).replace("\\", "/")
    except ValueError:
        return path


def work_dir(week, create=True):
    d = p("work", week)
    if create:
        os.makedirs(os.path.join(d, "pages"), exist_ok=True)
    return d


def read_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path, obj):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def write_text(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def append_jsonl(path, obj):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return out


def today():
    return dt.date.today()


def now_iso():
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], start=1)}


def parse_date(s):
    """Return a date from a string that starts with YYYY-MM-DD (ISO), else None."""
    if not s or not isinstance(s, str):
        return None
    m = re.match(r"\s*(\d{4})-(\d{2})-(\d{2})", s)
    if not m:
        return None
    try:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def parse_loose_date(s):
    """ISO, 'October 22, 2026', '22 Oct 2026', '22/10/2026' (day-first), or epoch ms/s."""
    if s is None:
        return None
    if isinstance(s, (int, float)):
        try:
            v = float(s)
            if v > 1e11:
                v /= 1000.0
            return dt.datetime.fromtimestamp(v, dt.timezone.utc).date()
        except (OverflowError, OSError, ValueError):
            return None
    s = str(s).strip()
    d = parse_date(s)
    if d:
        return d
    m = re.match(r"\s*(\d{4})/(\d{1,2})/(\d{1,2})", s)
    if m:
        try:
            return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None
    m = re.search(r"\b([A-Za-z]{3,9})\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})\b", s)
    if m and m.group(1)[:3].lower() in MONTHS:
        try:
            return dt.date(int(m.group(3)), MONTHS[m.group(1)[:3].lower()], int(m.group(2)))
        except ValueError:
            return None
    m = re.search(r"\b(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]{3,9})\.?,?\s+(\d{4})\b", s)
    if m and m.group(2)[:3].lower() in MONTHS:
        try:
            return dt.date(int(m.group(3)), MONTHS[m.group(2)[:3].lower()], int(m.group(1)))
        except ValueError:
            return None
    m = re.search(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b", s)
    if m:
        try:
            return dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        except ValueError:
            return None
    return None


def iso_week(d):
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def week_bounds(week):
    m = re.fullmatch(r"(\d{4})-W(\d{2})", week or "")
    if not m:
        raise ValueError(f"bad week id {week!r}; expected YYYY-Www")
    monday = dt.date.fromisocalendar(int(m.group(1)), int(m.group(2)), 1)
    return monday, monday + dt.timedelta(days=6)


TRACKING_PREFIXES = ("utm_", "oly_", "_hs", "mc_", "vero_", "pk_", "mtm_")
TRACKING_KEYS = {"fbclid", "gclid", "dclid", "yclid", "igshid", "ref_src", "ref_url", "cmpid", "ncid",
                 "sr_share", "smid", "ocid", "mkt_tok", "guccounter", "guce_referrer"}


def canonical_url(u):
    u = (u or "").strip()
    if not u:
        return u
    if u.startswith("http://"):
        u = "https://" + u[len("http://"):]
    if not u.startswith("https://"):
        return u
    parts = urllib.parse.urlsplit(u)
    host = (parts.hostname or "").lower()
    if parts.port and parts.port not in (80, 443):
        host = f"{host}:{parts.port}"
    query = []
    for k, v in urllib.parse.parse_qsl(parts.query, keep_blank_values=True):
        kl = k.lower()
        if kl.startswith(TRACKING_PREFIXES) or kl in TRACKING_KEYS:
            continue
        query.append((k, v))
    path = parts.path or "/"
    if len(path) > 1 and path.endswith("/"):
        path = path.rstrip("/")
    return urllib.parse.urlunsplit(("https", host, path, urllib.parse.urlencode(query), ""))


def url_id(u):
    return hashlib.sha1(canonical_url(u).encode("utf-8")).hexdigest()[:12]


def host_of(u):
    try:
        h = urllib.parse.urlsplit(u).hostname or ""
    except ValueError:
        return ""
    return h[4:] if h.startswith("www.") else h


def story_key(headline):
    s = re.sub(r"[^a-z0-9 ]+", " ", (headline or "").lower())
    s = re.sub(r"\s+", " ", s).strip()
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:12]


_QUOTE_MAP = str.maketrans({
    "‘": "'", "’": "'", "‚": "'", "‛": "'", "ʼ": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "–": "-", "—": "-", "−": "-", "‐": "-", "‑": "-", "­": "",
    " ": " ", " ": " ", " ": " ", " ": " ", " ": " ", " ": " ", " ": " ",
    "​": "", "‌": "", "‍": "", "﻿": "",
    "…": "...",
})


def norm_text(s):
    s = (s or "").translate(_QUOTE_MAP)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


_WORD_RE = re.compile(r"[A-Za-z0-9ऀ-ॿ][\w'ऀ-ॿ.%$-]*|[₹]\s?\d[\d,.]*")


def word_count(s):
    return len(_WORD_RE.findall(s or ""))


LINK_RE = re.compile(r"\[([^\]\n]+)\]\((https?://[^\s)]+)\)")
URL_RE = re.compile(r"https?://[^\s)\]>\"']+")


def strip_links(md):
    return LINK_RE.sub(lambda m: m.group(1), md)


FM_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n", re.S)


def parse_front_matter(text):
    """Return (fm_dict, body, fm_text). Values are raw strings with surrounding quotes removed."""
    m = FM_RE.match(text)
    if not m:
        return {}, text, ""
    fm_text = m.group(1)
    body = text[m.end():]
    fm = {}
    for line in fm_text.splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        fm[k.strip()] = v
    return fm, body, fm_text


def set_front_matter_value(text, key, value):
    """Replace or add `key: value` in the front matter of a markdown text (value written as given)."""
    m = FM_RE.match(text)
    if not m:
        return text
    lines = m.group(1).splitlines()
    done = False
    for i, line in enumerate(lines):
        if re.match(rf"\s*{re.escape(key)}\s*:", line):
            lines[i] = f"{key}: {value}"
            done = True
    if not done:
        lines.append(f"{key}: {value}")
    return "---\n" + "\n".join(lines) + "\n---\n" + text[m.end():]


def eprint(*a, **k):
    print(*a, file=sys.stderr, **k)


def git(*args, check=True):
    cmd = ["git", "-C", ROOT] + list(args)
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {(r.stderr or r.stdout).strip()}")
    return r


def gh(*args, check=True, input_text=None):
    cmd = ["gh"] + list(args)
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", input=input_text)
    if check and r.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {(r.stderr or r.stdout).strip()}")
    return r


def repo_slug():
    try:
        url = git("remote", "get-url", "origin").stdout.strip()
        m = re.search(r"github\.com[:/]([^/]+/[^/.]+?)(?:\.git)?$", url)
        if m:
            return m.group(1)
    except Exception:
        pass
    return REPO_SLUG
