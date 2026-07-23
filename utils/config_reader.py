import json
from pathlib import Path
from typing import Any, Optional


class ConfigReader:
    _instance = None

    _initialized: bool = False

    def __new__(cls, config_path: Optional[Path] = None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config_path: Optional[Path] = None):
        if ConfigReader._initialized:
            return

        if config_path is None:
            self._config_path = Path(__file__).parent.parent / "config.json"

        else:
            self._config_path = config_path

        self._config: dict[str, Any] = self._load_config()
        ConfigReader._initialized = True

    def _load_config(self):
        if not self._config_path.exists():
            raise FileNotFoundError(f"Config not found:{self._config_path}")
        with open(self._config_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get(self, key: str, default: Any = None) -> Any:
        """Получить значение по ключу верхнего уровня"""
        return self._config.get(key, default)

    def get_nested(self, *keys: str, default: Any = None) -> Any:
        current = self._config
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current


config = ConfigReader()
