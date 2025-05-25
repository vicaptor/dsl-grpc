
import os
import tempfile
import pytest
import numpy as np
from pathlib import Path
from unittest.mock import MagicMock, patch
from dsl_grpc.pipeline import Pipeline
from dsl_grpc.core.config import Config
from dsl_grpc.processors.base import BaseProcessor

# Mock processor for testing
class MockProcessor(BaseProcessor):
    def __init__(self, config):
        super().__init__(config)
        self.processed = False
    
    def process(self, frame):
        self.processed = True
        return {'success': True, 'frame_shape': frame.shape}

@pytest.fixture
def temp_config_file():
    """Create a temporary config file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("""
        pipeline:
          name: test-pipeline
          processing: []
        """)
    yield f.name
    os.unlink(f.name)

@pytest.fixture
def processor_config_file():
    """Create a config file with a test processor."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("""
        pipeline:
          name: test-pipeline
          processing:
            - type: mock
              params:
                param1: value1
        """)
    yield f.name
    os.unlink(f.name)

@pytest.fixture
def pipeline(temp_config_file):
    """Return a pipeline instance with no processors."""
    return Pipeline(Config(temp_config_file))

@pytest.fixture
def mock_processor():
    """Return a mock processor instance."""
    processor = MagicMock(spec=BaseProcessor)
    processor.process.return_value = {'success': True}
    return processor

@pytest.fixture
def mock_processor_class():
    """Return a mock processor class."""
    class MockProcessorClass:
        def __init__(self, config):
            self.config = config
            self.processed = False
        
        def process(self, frame):
            self.processed = True
            return {'success': True}
    
    return MockProcessorClass

def test_pipeline_initialization(pipeline):
    """Test that pipeline initializes correctly."""
    assert pipeline is not None
    assert hasattr(pipeline, 'processors')
    assert isinstance(pipeline.processors, list)
    assert len(pipeline.processors) == 0

def test_process_frame_without_processors(pipeline):
    """Test processing a frame with no processors."""
    # Create a test frame
    test_frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Process the frame
    results = pipeline.process_frame(test_frame)
    
    # Verify results
    assert isinstance(results, list)
    assert len(results) == 0

def test_process_frame_with_processor(pipeline, mock_processor):
    """Test processing a frame with one processor."""
    # Add mock processor to pipeline
    pipeline.processors = [mock_processor]
    
    # Create a test frame
    test_frame = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Process the frame
    results = pipeline.process_frame(test_frame)
    
    # Verify results
    assert isinstance(results, list)
    assert len(results) == 1
    assert results[0] == {'success': True}
    mock_processor.process.assert_called_once_with(test_frame)

@patch('dsl_grpc.pipeline.Pipeline._create_processor')
def test_processor_creation(mock_create_processor, processor_config_file):
    """Test that processors are created correctly from config."""
    # Setup mock
    mock_processor = MagicMock()
    mock_processor.process.return_value = {'success': True}
    mock_create_processor.return_value = mock_processor
    
    # Create pipeline
    pipeline = Pipeline(Config(processor_config_file))
    
    # Verify processor was created
    assert len(pipeline.processors) == 1
    mock_create_processor.assert_called_once()

def test_pipeline_with_multiple_processors(tmp_path, mock_processor_class):
    """Test pipeline with multiple processors."""
    # Create a config file with multiple processors
    config_path = tmp_path / "pipeline_config.yaml"
    config_path.write_text("""
    pipeline:
      name: multi-processor-pipeline
      processing:
        - type: processor1
          params: {}
        - type: processor2
          params: {}
    """)
    
    # Patch the processor creation
    with patch('dsl_grpc.pipeline.Pipeline._create_processor') as mock_create_processor:
        # Setup mock processors
        mock_processor1 = MagicMock()
        mock_processor2 = MagicMock()
        mock_processor1.process.return_value = {'result': 'processor1'}
        mock_processor2.process.return_value = {'result': 'processor2'}
        mock_create_processor.side_effect = [mock_processor1, mock_processor2]
        
        # Create and test pipeline
        pipeline = Pipeline(Config(str(config_path)))
        results = pipeline.process_frame(np.zeros((100, 100, 3), dtype=np.uint8))
        
        # Verify results
        assert len(results) == 2
        assert results[0] == {'result': 'processor1'}
        assert results[1] == {'result': 'processor2'}
        mock_processor1.process.assert_called_once()
        mock_processor2.process.assert_called_once()
