import datetime
import json
import os
from pathlib import Path

import sh
from rich.console import Console
from typer import Typer

generate = Typer()
console = Console()


@generate.callback()
def generate_callback():
    """Generate code."""


@generate.command()
def compare_themes():
    """Compare MkDocs themes."""
    json_fields = [
        'fullName',
        'isArchived',
        'isDisabled',
        'name',
        'owner',
        'pushedAt',
        'stargazersCount',
        'url',
    ]

    relative_path = 'docs/material/.generated'

    output_path = Path(__file__).parent.parent / relative_path

    console.print(f'GitHub CLI → [code]{relative_path}[/code]…  ', end='')
    raw_response = sh.gh.search.repos(
        'mkdocs',
        'theme',
        archived='false',
        limit=10,
        sort='stars',
        json=','.join(json_fields),
        _env={
            **os.environ,
            'NO_COLOR': '1',
        },
    )

    (output_path / 'github-themes.json').write_text(
        json.dumps(
            json.loads(raw_response),
            indent=2,
        ),
    )

    (output_path / 'date.json').write_text(
        json.dumps(
            {
                '@id': 'github-themes-generation-date',
                'rdfs:label': str(datetime.date.today()),
            },
            indent=2,
        ),
    )

    console.print('[OK]', style='green')


@generate.command()
def cover_image():
    """Generate cover image for the front page."""
    assets = Path(__file__).parent.parent / 'docs/assets'
    sh.convert(
        assets / 'cover-original.png',
        '-crop', 'x300+0+300',
        assets / 'cover.png',
    )


@generate.command()
def icon():
    """Generate site icon image."""
    assets = Path(__file__).parent.parent / 'docs/assets'
    sh.convert(
        assets / 'icon-original.png',
        '-scale', 'x128',
        assets / 'icon.png',
    )
