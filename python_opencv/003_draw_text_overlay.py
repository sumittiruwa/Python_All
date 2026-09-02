"""OpenCV Practice: Draw Text Overlay"""

import cv2
import numpy as np


def draw_text(canvas, text, position, font, scale, color, thickness):
    cv2.putText(canvas, text, position, font, scale, color, thickness)
    return canvas


def build_demo_canvas():
    canvas = np.zeros((150, 300, 3), dtype=np.uint8)
    draw_text(canvas, "Hello", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    draw_text(canvas, "OpenCV", (10, 80), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 1)
    draw_text(canvas, "Practice", (10, 130), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (0, 128, 255), 1)
    return canvas


if __name__ == "__main__":
    canvas = build_demo_canvas()
    size, baseline = cv2.getTextSize("Hello", cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)
    print("Canvas shape:", canvas.shape)
    print("Text size for 'Hello':", size, "baseline:", baseline)
    print("Non-zero pixels after drawing text:", int(np.count_nonzero(canvas)))
