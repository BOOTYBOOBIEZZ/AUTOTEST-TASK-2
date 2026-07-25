import pytest

from tests.test_filter import config


class ConfigError(Exception):
    pass


@pytest.fixture(scope="session")
def base_url():
    url = config.get_nested("urls", "base_url")
    print(f"\n[DEBUUG] base_url loaded: {url}\n")
    if url is None:
        raise ConfigError("base_url not found in config.json!")


@pytest.fixture(scope="session")
def search_url():
    url = config.get_nested("urls", "search_url")
    print(f"\n[DEBUUG] search_url loaded: {url}\n")
    if url is None:
        raise ConfigError("search_url not found in config.json!")
