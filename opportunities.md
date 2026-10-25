---
layout: default
title: Opportunities
permalink: /opportunities/
---
# Open opportunities

Internships, fellowships, campus programmes and competitions worth a pre-final-year CS student's time. Every row was opened and checked on the date in the last column; rows whose deadline has passed are removed each week. The India edition carries the five soonest deadlines.

{% assign dated = site.data.opportunities | where_exp: "o", "o.deadline != 'rolling'" | sort: "deadline" %}
{% assign rolling = site.data.opportunities | where: "deadline", "rolling" %}

{% if dated.size == 0 and rolling.size == 0 %}
*Nothing listed yet. Rows appear after the first weekly run.*
{% endif %}

{% if dated.size > 0 %}
## With a deadline

<table>
<thead><tr><th>Deadline</th><th>What</th><th>Type</th><th>For</th><th>Note</th><th>Checked</th></tr></thead>
<tbody>
{% for o in dated %}
<tr><td class="nowrap">{{ o.deadline | date: "%-d %b %Y" }}{% if o.status == "expected" %} <span class="tag">expected</span>{% endif %}</td><td><a href="{{ o.url }}">{{ o.title }}</a><br><span class="meta small">{{ o.org }}</span></td><td>{{ o.type }}</td><td>{{ o.audience }}</td><td>{{ o.note }}</td><td class="nowrap small">{{ o.verified_on | date: "%-d %b" }}</td></tr>
{% endfor %}
</tbody>
</table>
{% endif %}

{% if rolling.size > 0 %}
## Rolling

<table>
<thead><tr><th>What</th><th>Type</th><th>For</th><th>Note</th><th>Checked</th></tr></thead>
<tbody>
{% for o in rolling %}
<tr><td><a href="{{ o.url }}">{{ o.title }}</a><br><span class="meta small">{{ o.org }}</span></td><td>{{ o.type }}</td><td>{{ o.audience }}</td><td>{{ o.note }}</td><td class="nowrap small">{{ o.verified_on | date: "%-d %b" }}</td></tr>
{% endfor %}
</tbody>
</table>
{% endif %}
