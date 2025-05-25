
from abc import ABC, abstractmethod
from typing import Dict, Any
import numpy as np

class BaseProcessor(ABC):
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    def process(self, frame: np.ndarray) -> Dict[str, Any]:
        pass
