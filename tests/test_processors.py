
import pytest
import numpy as np
from dsl_grpc.processors.base import BaseProcessor

# Test processor implementation
class MockProcessor(BaseProcessor):
    def __init__(self, config):
        super().__init__(config)
        self.processed = False
    
    def process(self, frame):
        self.processed = True
        return {'success': True, 'shape': frame.shape}

@pytest.fixture
def processor_config():
    return {'param1': 'value1'}

@pytest.fixture
def processor(processor_config):
    return MockProcessor(processor_config)

def test_processor_initialization(processor, processor_config):
    assert isinstance(processor, BaseProcessor)
    assert processor.config == processor_config
    assert not processor.processed

def test_processor_process(processor):
    # Create a test frame
    test_frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Process the frame
    result = processor.process(test_frame)
    
    # Verify results
    assert processor.processed
    assert isinstance(result, dict)
    assert result['success'] is True
    assert result['shape'] == (100, 100, 3)
