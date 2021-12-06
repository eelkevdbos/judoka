import os
from unittest.mock import patch

from judoka import config


def test_loading_default_home_folder_config():
    with patch.object(config, "home_config", "tests/fixtures/greeter.toml"):
        c = config.load()
    assert c == {"greet": "echo 'hi'"}


def test_loading_custom_home_folder_config():
    with patch.dict(os.environ, {"JUDOKA_HOME": "tests/fixtures/singer.toml"}):
        c = config.load()
    assert c == {"sing": "echo 'doremifasoladi'"}


def test_disable_loading_home_folder_config():
    with patch.dict(os.environ, {"JUDOKA_HOME": ""}):
        c = config.load()
    assert c == {}


def test_loading_project_config():
    with patch.object(config, "project_config", "tests/fixtures/dancer.toml"):
        c = config.load()
    assert c == {"dance": "echo 'taptaptap'"}


def test_loading_additional_config_paths():
    c = config.load("tests/fixtures/dreamer.toml")
    assert c == {"dream": "echo 'zzzzz'"}
