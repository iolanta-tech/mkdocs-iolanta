---
title: mkdocs-iolanta
hide:
  - toc
---

> Integrate [MkDocs](https://mkdocs.org) static site builder with [iolanta](https://iolanta.tech) Linked Data visualization framework.

## Features

Visualize:

* Links,
* Tables,
* Roadmaps
* …and more

on your MkDocs static site!


## Installation

Python ⩾ 3.10 is required.

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
3. This enables [mkdocs-macros-plugin](https://mkdocs-macros-plugin.readthedocs.io) which is required to utilize Iolanta capabilities on MkDocs pages, such as {{ render("render") }} macro.
4. This setting is highly recommended. If there is an error during rendering MkDocs macros, including those macros provided by Iolanta, the site build will throw an error — making the issue easier to notice both on local development and in CI.
