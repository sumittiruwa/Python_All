"""OpenCV Practice: Resize Preserving Aspect Ratio with Letterbox Padding"""

import cv2
import numpy as np


def make_image(h=120, w=300):
    img = np.full((h, w, 3), (60, 120, 180), dtype=np.uint8)
    cv2.rectangle(img, (20, 20), (w - 20, h - 20), (255, 255, 255), 2)
    return img


def letterbox_resize(img, target_size=200, pad_color=(0, 0, 0)):
    h, w = img.shape[:2]
    scale = target_size / max(h, w)
    new_w, new_h = int(round(w * scale)), int(round(h * scale))
    resized = cv2.resize(img, (new_w, new_h))

    canvas = np.full((target_size, target_size, 3), pad_color, dtype=np.uint8)
    y_off = (target_size - new_h) // 2
    x_off = (target_size - new_w) // 2
    canvas[y_off:y_off + new_h, x_off:x_off + new_w] = resized
    return canvas, (x_off, y_off, new_w, new_h)


if __name__ == "__main__":
    img = make_image()
    canvas, box = letterbox_resize(img, target_size=200)

    print("Original shape:", img.shape)
    print("Letterboxed shape:", canvas.shape)
    print("Content box (x, y, w, h):", box)
