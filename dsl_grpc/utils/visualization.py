
import cv2
import numpy as np
from typing import List, Dict, Any

class Visualizer:
    def __init__(self):
        self.colors = self._generate_colors()

    def _generate_colors(self, num_colors: int = 80):
        """Generate random colors for visualization"""
        return np.random.randint(0, 255, size=(num_colors, 3), dtype=np.uint8)

    def draw_detections(self, frame: np.ndarray, detections: List[Dict[str, Any]]) -> np.ndarray:
        """Draw detection boxes and labels on frame"""
        img = frame.copy()
        for det in detections:
            bbox = det['bbox']
            label = det['class_name']
            conf = det['confidence']
            color = self.colors[hash(label) % len(self.colors)]

            # Draw rectangle
            cv2.rectangle(img, 
                (int(bbox[0]), int(bbox[1])),
                (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])),
                color.tolist(), 2)

            # Draw label
            text = f"{label}: {conf:.2f}"
            cv2.putText(img, text,
                (int(bbox[0]), int(bbox[1] - 5)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color.tolist(), 2)

        return img

    def draw_tracks(self, frame: np.ndarray, tracks: List[Dict[str, Any]]) -> np.ndarray:
        """Draw tracking information on frame"""
        img = frame.copy()
        for track in tracks:
            track_id = track['track_id']
            bbox = track['bbox']
            color = self.colors[track_id % len(self.colors)]

            # Draw rectangle
            cv2.rectangle(img,
                (int(bbox[0]), int(bbox[1])),
                (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])),
                color.tolist(), 2)

            # Draw ID
            cv2.putText(img, str(track_id),
                (int(bbox[0]), int(bbox[1] - 5)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color.tolist(), 2)

        return img
