# dsl_grpc

## License

```
#
# Copyright 2025 Tom Sapletta <info@softreck.dev>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
```

## Author
- Tom Sapletta <info@softreck.dev>

dsl based on gRPC protocoll to buidl process by API

# Camera AI Pipeline System

## Project Structure
```
dsl_grpc/
│
├── README.md
├── LICENSE
├── setup.py
├── requirements.txt
├── docker-compose.yml
├── .env
│
├── configs/
│   ├── pipeline_config.yaml
│   ├── logging_config.yaml
│   └── models_config.yaml
│
├── docs/
│   ├── installation.md
│   ├── configuration.md
│   ├── api.md
│   ├── processors.md
│   └── deployment.md
│
├── dsl_grpc/
│   ├── __init__.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logging.py
│   │   └── exceptions.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── pipeline.py
│   │   ├── executor.py
│   │   └── scheduler.py
│   │
│   ├── processors/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── object_detection.py
│   │   ├── face_detection.py
│   │   ├── motion_detection.py
│   │   ├── license_plate.py
│   │   ├── crowd_counting.py
│   │   └── custom.py
│   │
│   ├── streaming/
│   │   ├── __init__.py
│   │   ├── rtsp_client.py
│   │   ├── grpc_server.py
│   │   └── rss_publisher.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── model_loader.py
│   │   └── model_registry.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── visualization.py
│       ├── metrics.py
│       └── helpers.py
│
├── tests/
│   ├── __init__.py
│   ├── test_pipeline.py
│   ├── test_processors.py
│   ├── test_streaming.py
│   └── test_models.py
│
├── scripts/
│   ├── install_dependencies.sh
│   ├── download_models.sh
│   └── run_tests.sh
│
└── examples/
    ├── basic_pipeline.py
    ├── custom_processor.py
    └── distributed_processing.py
```

Now, let's create a comprehensive README:


# Camera AI Pipeline System

A flexible and scalable system for real-time video processing with multiple AI models and streaming capabilities.

## Features

- **Multiple Processing Types:**
  - Object Detection
  - Face Detection
  - Motion Detection
  - License Plate Recognition
  - Crowd Counting
  - Custom Processing Support

- **Flexible Pipeline Configuration:**
  - YAML-based configuration
  - Dynamic processor loading
  - Custom processor support
  - Multiple input/output streams

- **Streaming Support:**
  - RTSP input
  - gRPC processing
  - RSS feed output
  - RTMP streaming

- **Performance:**
  - GPU acceleration
  - Async processing
  - Batch processing
  - Memory management

## Installation

### Prerequisites

- Python 3.8+
- CUDA 11.0+ (for GPU support)
- FFmpeg
- OpenCV
- Docker & Docker Compose (for containerized deployment)

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dsl_grpc.git
cd dsl_grpc
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download pre-trained models:
```bash
./scripts/download_models.sh
```

4. Configure your pipeline:
```bash
cp configs/pipeline_config.yaml.example configs/pipeline_config.yaml
# Edit pipeline_config.yaml with your settings
```

5. Run the pipeline:
```bash
python -m dsl_grpc
```

### Docker Deployment

1. Build and start services:
```bash
docker-compose up -d
```

2. Monitor logs:
```bash
docker-compose logs -f
```

## Configuration

### Pipeline Configuration

Example pipeline configuration:
```yaml
pipeline:
  name: traffic-monitoring
  source:
    uri: rtsp://camera.example.com/stream
    protocol: rtsp
    credentials:
      username: admin
      password: pass123
  
  processing:
    - type: object_detection
      model_path: /models/yolov5s.pt
      confidence: 0.5
      params:
        classes: [2, 5, 7]  # car, bus, truck
    
    - type: license_plate
      model_path: /models/plate_detector.pt
      confidence: 0.6
  
  output:
    - type: rss
      uri: http://events.example.com/feed
      format: xml
```

### Environment Variables

Copy `.env.example` to `.env` and configure:
```bash
cp .env.example .env
# Edit .env with your settings
```

## Usage

### Basic Usage

```python
from dsl_grpc import Pipeline

# Load pipeline from config
pipeline = Pipeline.from_config('configs/pipeline_config.yaml')

# Start processing
pipeline.start()
```

### Custom Processor

```python
from dsl_grpc.processors import BaseProcessor, ProcessingResult

class MyCustomProcessor(BaseProcessor):
    def process(self, frame):
        # Custom processing logic
        return ProcessingResult(...)

# Register custom processor
pipeline.register_processor('custom', MyCustomProcessor)
```

## API Documentation

### Pipeline DSL

The Pipeline DSL provides a flexible way to configure processing pipelines:
- Input stream configuration
- Processing steps definition
- Output stream settings

See [Pipeline DSL Documentation](docs/pipeline_dsl.md) for details.

### Processing Types

Each processor type has specific configuration options:

- **Object Detection:**
  - Model selection
  - Confidence thresholds
  - Class filtering

- **Face Detection:**
  - Landmark detection
  - Face attributes
  - Minimum face size

- **License Plate:**
  - Region settings
  - OCR configuration
  - Plate validation

See [Processors Documentation](docs/processors.md) for details.

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

```bash
black dsl_grpc
isort dsl_grpc
flake8 dsl_grpc
```

### Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Performance Optimization

- Enable GPU acceleration
- Adjust batch size
- Configure processing queue
- Optimize model inference

See [Performance Guide](docs/performance.md) for details.

## Monitoring

- Prometheus metrics
- Grafana dashboards
- Performance monitoring
- Error tracking

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- YOLOv5
- MediaPipe
- OpenCV
- Tesseract OCR
- CSRNet



To use this script:

1. Save it as `gen.py`

2. Create a new project:
```bash
python gen.py
```

The script will:
1. Create complete directory structure
2. Generate all necessary files
3. Initialize git repository
4. Install dependencies
5. Set up development environment

Features:
- Modular code generation
- Configuration files
- Documentation
- Docker setup
- Testing framework
- Example code
- Development tools

The generated project follows:
- Best practices
- Clean architecture
- Modern Python conventions
- Docker integration
- CI/CD ready

Would you like me to:
1. Add more file templates?
2. Include additional configuration options?
3. Add more example code?
4. Include CI/CD templates?