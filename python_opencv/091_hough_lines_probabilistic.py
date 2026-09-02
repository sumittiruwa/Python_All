"""OpenCV Practice: Probabilistic Hough Lines Transform"""

import cv2
import numpy as np


def make_line_segments_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.line(img, (10, 20), (90, 20), 255, 2)
    cv2.line(img, (10, 80), (60, 80), 255, 2)
    return img


def detect_line_segments(img, threshold=30, min_len=20, max_gap=5):
    return cv2.HoughLinesP(img, 1, np.pi / 180, threshold, minLineLength=min_len, maxLineGap=max_gap)


if __name__ == "__main__":
    image = make_line_segments_image()
    segments = detect_line_segments(image)

    count = 0 if segments is None else len(segments)
    print("Line segments detected:", count)
    if segments is not None:
        for line in segments.reshape(-1, 4)[:5]:
            x1, y1, x2, y2 = line
            length = round(float(np.hypot(x2 - x1, y2 - y1)), 2)
            print(f"({x1},{y1}) -> ({x2},{y2}), length={length}")
