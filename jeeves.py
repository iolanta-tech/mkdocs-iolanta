from sh import mkdocs


def serve():
    mkdocs(
        'serve', '-a', 'localhost:9841',
        _fg=True,
    )
