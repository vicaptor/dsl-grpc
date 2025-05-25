
import cv2
import asyncio
from typing import AsyncIterator
import numpy as np
import logging

class RTSPClient:
    def __init__(self, url: str, **kwargs):
        self.url = url
        self.kwargs = kwargs
        self.cap = None
        self.logger = logging.getLogger(__name__)

    async def connect(self) -> bool:
        """Connect to RTSP stream"""
        try:
            self.cap = cv2.VideoCapture(self.url)
            if not self.cap.isOpened():
                self.logger.error(f"Failed to connect to {self.url}")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Error connecting to RTSP stream: {e}")
            return False

    async def get_frames(self) -> AsyncIterator[np.ndarray]:
        """Get frames from RTSP stream"""
        if not self.cap:
            raise RuntimeError("Not connected to RTSP stream")

        while True:
            ret, frame = self.cap.read()
            if not ret:
                self.logger.warning("Failed to read frame")
                await asyncio.sleep(0.1)
                continue
            yield frame
            await asyncio.sleep(1/30)  # 30 FPS

    async def close(self):
        """Close RTSP connection"""
        if self.cap:
            self.cap.release()
