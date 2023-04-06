import funcy
import pytest
from iolanta.iolanta import Iolanta
from iolanta.namespaces import IOLANTA, LOCAL
from rdflib import URIRef


@pytest.fixture()
def environment() -> URIRef:
    return IOLANTA.html


@pytest.fixture()
def node() -> URIRef:
    return LOCAL.test


def test_icon(node: URIRef, environment: URIRef):
    response = str(
        funcy.first(
            Iolanta().add({
                '$id': 'test',
                'mkdocs-material:icon': 'simple/iced.svg',
            }).render(
                node,
                environments=[environment],
            ),
        ),
    )

    assert response.startswith('<span class="twemoji"><svg')
    assert response.endswith('</svg></span> Test')
