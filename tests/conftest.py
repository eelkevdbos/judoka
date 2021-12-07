import os
from unittest.mock import patch

import pytest as pytest

from judoka import config


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    # prevent local judo-use to bleed into tests via environment or home config
    empty_environment = patch.dict(os.environ, {})
    empty_home_config = patch.object(config, "home_config", "/tmp/.judorc")

    with empty_environment, empty_home_config:
        yield
