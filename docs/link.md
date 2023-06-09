---
title: Linking to pages
---

Insert links to pages and maintain their correctness even when moving `.md` files all over the place.

## Assign [`$id`](https://iolanta.tech/vocabularies/id/) to a page

Using YAML frontmatter:

{{ code("render.md", last_line=5, language="markdown") }}

## Then call the page

{% raw %}
```jinja2
{{ render("render") }}
```
{% endraw %}

## This yields a link to the said page

Here it is: {{ render("render") }}.
