---
title: "mkdocs-material:template"
hide:
  - toc
---

# How to use custom HTML/Jinja2 template per page

[:simple-github: mkdocs-material](https://github.com/squidfunk/mkdocs-material) handles `template` YAML [frontmatter property](https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-template). For instance, we have a `templates/announce.html` template file which we want to use on this page. To use it, we can write:

```markdown title="our_page.md"
---
template: announce.html
---

Markdown content…
```

## `mkdocs-material:template` RDF property

Alternatively, we can state the following anywhere in the site.

{{ code("material/template.yaml", language="yaml") }}

## Assign custom template to multiple pages at once

Use the power of [:owl: OWL](https://www.w3.org/TR/owl2-overview/).

```yaml
$id: PageWithCustomTemplateClass
owl:equivalentClass:
  $type: owl:Restriction
  owl:onProperty:
    $id: mkdocs-material:template
  owl:hasValue:
    $id: custom_template.html
```

Then, you need to ensure that each page in question has `PageWithCustomTemplateClass` assigned. This can be done via `$type` declaration or perhaps with more OWL magic.
