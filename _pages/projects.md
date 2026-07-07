---
permalink: /projects/
title: "Projects"
excerpt: ""
author_profile: true
---

<span class='anchor' id='projects'></span>

# 🏢 Industry Projects

{% for project in site.data.projects.industry %}
{% include project-card.html project=project %}
{% endfor %}

{% if site.data.projects.personal and site.data.projects.personal.size > 0 %}
# 💡 Personal Projects

{% for project in site.data.projects.personal %}
{% include project-card.html project=project %}
{% endfor %}
{% endif %}
