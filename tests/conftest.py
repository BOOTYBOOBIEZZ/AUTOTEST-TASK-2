import pytest

from utils.config_reader import ConfigReader


class ConfigError(Exception):
    pass


@pytest.fixture(scope="session")
def config():
    return ConfigReader()


@pytest.fixture(scope="session")
def base_url(config: ConfigReader):
    url = config.get_nested("urls", "base_url")
    print(f"\n[DEBUUG] base_url loaded: {url}\n")
    if not url:
        raise ConfigError("base_url not found in config.json!")
    return url


@pytest.fixture(scope="session")
def search_url(config: ConfigReader):
    url = config.get_nested("urls", "search_url")
    print(f"\n[DEBUUG] search_url loaded: {url}\n")
    if not url:
        raise ConfigError("search_url not found in config.json!")
    return url
