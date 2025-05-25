
import os
from pathlib import Path
from typing import Dict, Any
import yaml

class Config:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        with open(self.config_path) as f:
            return yaml.safe_load(f)

    @property
    def pipeline_config(self) -> Dict[str, Any]:
        return self.config['pipeline']
