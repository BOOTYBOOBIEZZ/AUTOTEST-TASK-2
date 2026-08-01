import json
from pathlib import Path
from typing import Any


class ConfigReader:
    _instances: dict[str, "ConfigReader"] = {}
    _config_path: Path
    _config: dict[str, Any]

    def __new__(cls, config_path: str | Path | None = None) -> "ConfigReader":
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config.json"

        config_path = str(Path(config_path).resolve())

        if config_path not in cls._instances:
            instance = super().__new__(cls)
            instance._config_path = Path(config_path)
            instance._config = instance._load()
            cls._instances[config_path] = instance

        return cls._instances[config_path]

    def _load(self) -> dict[str, Any]:
        if not self._config_path.exists():
            raise FileNotFoundError(f"Config not found: {self._config_path}")

        with open(self._config_path, encoding="utf-8") as file:
            return json.load(file)

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def get_nested(self, *keys: str, default: Any = None) -> Any:
        current = self._config
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current
