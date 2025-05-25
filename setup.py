
from setuptools import setup, find_packages

setup(
    name="dsl_grpc",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
        "torch>=1.9.0",
        "grpcio>=1.40.0",
        "pyyaml>=5.4.0",
        "mediapipe>=0.8.0",
        "pytesseract>=0.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0.0",
            "isort>=5.0.0",
            "flake8>=3.9.0",
        ]
    },
    python_requires=">=3.8",
)
