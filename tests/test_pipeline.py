
import pytest
import numpy as np
from dsl_grpc.pipeline import Pipeline
from dsl_grpc.core.config import Config

@pytest.fixture
def config():
    return {
        'pipeline': {
            'name': 'test-pipeline',
            'processing': []
        }
    }

@pytest.fixture
def pipeline(config):
    return Pipeline(Config(config))

def test_pipeline_initialization(pipeline):
    assert pipeline is not None
    assert len(pipeline.processors) == 0

def test_process_frame(pipeline):
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    results = pipeline.process_frame(frame)
    assert isinstance(results, list)
