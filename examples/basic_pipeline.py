
import asyncio
from dsl_grpc import Pipeline
from dsl_grpc.core.config import Config

async def main():
    # Load configuration
    config = Config('configs/pipeline_config.yaml')

    # Initialize pipeline
    pipeline = Pipeline(config)

    # Process video stream
    async with pipeline:
        async for frame in pipeline.get_frames():
            results = pipeline.process_frame(frame)
            print("Processed frame with {} detections".format(len(results)))

if __name__ == '__main__':
    asyncio.run(main())
