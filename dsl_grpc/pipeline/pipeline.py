
from typing import List, Dict, Any
from ..core.config import Config
from ..processors.base import BaseProcessor

class Pipeline:
    def __init__(self, config: Config):
        self.config = config
        self.processors: List[BaseProcessor] = []
        self._initialize_processors()

    def _initialize_processors(self):
        for proc_config in self.config.pipeline_config['processing']:
            processor = self._create_processor(proc_config)
            self.processors.append(processor)

    def _create_processor(self, config: Dict[str, Any]) -> BaseProcessor:
        # Processor creation logic
        pass

    def process_frame(self, frame):
        results = []
        for processor in self.processors:
            result = processor.process(frame)
            results.append(result)
        return results
