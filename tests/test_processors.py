
import pytest
import numpy as np
from dsl_grpc.processors.base import BaseProcessor

class TestProcessor(BaseProcessor):
    def process(self, frame):
        return {'result': True}

@pytest.fixture
def processor():
    return TestProcessor({})

def test_processor_initialization(processor):
    assert isinstance(processor, BaseProcessor)

def test_process_frame(processor):
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    result = processor.process(frame)
    assert isinstance(result, dict)
    assert result['result'] is True
