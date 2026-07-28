import json
from pathlib import Path
from typing import Any


class ConfigReader:
    _instances: dict[Path, "ConfigReader"] = {}

    def __new__(cls, config_path: Path | None = None):
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config.json"
        else:
            config_path = Path(config_path).resolve()

        if config_path in cls._instances:
            return cls._instances[config_path]

        instance = super().__new__(cls)
        cls._instances[config_path] = instance
        return instance

    def __init__(self, config_path: Path | None = None):
        if self._config is None:
            return

        if config_path is None:
            self._config_path = Path(__file__).parent.parent / "config.json"

        else:
            self._config_path = Path(config_path).resolve()

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
