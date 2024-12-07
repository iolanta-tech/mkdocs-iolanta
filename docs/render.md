---
title: "Render: macro"
$id: render
---

# `{% raw %}{{ render }}{% endraw %}` macro

On any Markdown page on your MkDocs site, you can now use `render()` macro. For instance, here is a YAML file:

{{ code("plugins.yaml", language="yaml") }}

and here is a Markdown file:

{% raw %}
```markdown
{{ render('plugins') }}
```
{% endraw %}

That yields:

```
{% raw %}
{{ render('plugins') }}
{% endraw %}
``` 

…as rendered via [iolanta-tables](https://iolanta.tech/tables).

```shell title="Install iolanta-tables to reproduce this example!"
pip install iolanta-tables
```
