import os
import pathlib
import typing as t

import toml


home_config = pathlib.Path("~/.judorc").expanduser()
project_config = pathlib.Path(".judorc")


def _load_file(path: t.Union[str, os.PathLike]) -> dict:
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)

    if not path.exists():
        return {}

    if not path.is_file():
        return {}

    with path.open() as f:
        return toml.load(f)


def load(*paths):
    config = {}

    # by default loads the judoka config present in the home folder
    # setting the environment variable to JUDOKA_HOME="" disables it
    config.update(_load_file(path=os.getenv("JUDOKA_HOME", home_config)))

    config.update(_load_file(path=project_config))

    for path in paths:
        config.update(_load_file(path))

    return config
