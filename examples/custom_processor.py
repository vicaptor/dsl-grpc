
from dsl_grpc.processors.base import BaseProcessor
import numpy as np
import cv2

class CustomProcessor(BaseProcessor):
    def __init__(self, config):
        super().__init__(config)
        self.threshold = config.get('threshold', 0.5)

    def process(self, frame: np.ndarray):
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply threshold
        _, binary = cv2.threshold(gray, int(self.threshold * 255), 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Process contours
        results = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100:  # Minimum area threshold
                x, y, w, h = cv2.boundingRect(contour)
                results.append({
                    'bbox': (x, y, w, h),
                    'area': area,
                    'confidence': 1.0
                })

        return results

# Example usage
if __name__ == '__main__':
    # Create processor
    processor = CustomProcessor({'threshold': 0.7})

    # Open video capture
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process frame
        results = processor.process(frame)

        # Draw results
        for result in results:
            x, y, w, h = result['bbox']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Show frame
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
