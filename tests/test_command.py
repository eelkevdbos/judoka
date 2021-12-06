from click import Context, Command

from judoka.command import Hub
from judoka.config import load


def test_hub_lists_commands():
    hub = Hub(config=load("tests/fixtures/greeter.toml"))
    assert ["greet"] == hub.list_commands(Context(hub))


def test_hub_get_command_returns_command():
    hub = Hub(config=load("tests/fixtures/greeter.toml"))
    command = hub.get_command(Context(hub), "greet")
    assert isinstance(command, Command)


def test_hub_is_configurable_via_config_injection():
    expected_config = {"answer": "echo '42'"}
    hub = Hub(config=expected_config)
    assert hub.config == expected_config


def test_hub_is_configurable_via_configresolver_injection():
    expected_config = {"answer": "echo '42'"}
    hub = Hub(configresolver=lambda: expected_config)
    assert hub.config == expected_config
