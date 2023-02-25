---
title: mkdocs-iolanta
hide:
  - navigation
---

Integrate [MkDocs](https://mkdocs.org) static site builder with [iolanta](https://iolanta.tech) Linked Data visualization toolbox.

## Prerequisites

* Python ⩾ 3.10
* Install [MkDocs](https://mkdocs.org) as per [tutorial](https://www.mkdocs.org/getting-started/).

## Installation

```shell
pip install mkdocs-iolanta
```

## Configuration

Open your `mkdocs.yml` configuration file and configure its `plugins` as follows:

```yaml
plugins:
  - search                  # (1)!
  - …
  - iolanta                 # (2)!
  - macros:                 # (3)!
      on_error_fail: true   # (4)!
  - …
```

1. The `search` plugin is built-in and automatically enabled if `mkdocs.yml` does not specify any `plugins` at all. But if it does, this built-in plugin must be enabled explicitly.
2. Support `iolanta` capabilities for this documentation site.
3. This enables [mkdocs-macros-plugin](https://mkdocs-macros-plugin.readthedocs.io) which is required to utilize Iolanta capabilities on MkDocs pages.
4. This setting is highly recommended. If there is an error during rendering MkDocs macros, including those macros provided by Iolanta, the site build will throw an error — making the issue easier to notice both on local development and in CI.

## Usage

On any Markdown page on your MkDocs site, you can now use `render()` macro. For instance, here is a YAML file:

```yaml
$id: plugins
table:columns:
  - plugin
  - description
table:rows:
  - plugin:
      rdfs:label: iolanta-tables
      schema:url: https://iolanta.tech/tables/
    description: Render HTML tables on your MkDocs site from YAML descriptions instead of clumsy Markdown markup
```

and here is a Markdown file:

{% raw %}
```markdown
{{ render('plugins') }}
```
{% endraw %}

That yields: {{ render('plugins') }} 

Follow the links to learn how to embed rich content into your MkDocs static site through Iolanta.
