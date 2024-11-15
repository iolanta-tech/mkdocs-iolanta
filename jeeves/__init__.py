from sh import mkdocs

from jeeves.generate import generate


def serve():
    mkdocs.serve(
        '-a', 'localhost:9841',
        _fg=True,
    )


__all__ = ['generate', 'serve']
