import pytest
from utils.config_reader import config


@pytest.fixture(scope="session")
def base_url():
    url = config.get_nested("urls", "base_url")
    print(f"\n[DEBUUG] base_url loaded: {url}\n")
    assert url, "base_url not found in config.json!"
    return url
