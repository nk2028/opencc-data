from __future__ import annotations

from importlib import resources
from importlib.metadata import PackageNotFoundError, version
from pathlib import PurePosixPath


try:
    __version__ = version("opencc-data")
except PackageNotFoundError:
    __version__ = "0.0.0"


def data_path(filename: str | None = None):
    base = resources.files(__name__).joinpath("data")
    return base if filename is None else base.joinpath(PurePosixPath(filename))


def config_path(filename: str | None = None):
    base = data_path("config")
    return base if filename is None else base.joinpath(PurePosixPath(filename))


def test_data_path(filename: str | None = None):
    base = resources.files(__name__).joinpath("test_data")
    return base if filename is None else base.joinpath(PurePosixPath(filename))


__all__ = ["__version__", "config_path", "data_path", "test_data_path"]
