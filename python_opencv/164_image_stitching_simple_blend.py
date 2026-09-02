"""OpenCV Practice: Simple Side-by-Side Homography Warp + Blend"""

import cv2
import numpy as np


def make_tile(color, size=150):
    img = np.full((size, size, 3), color, dtype=np.uint8)
    cv2.circle(img, (size // 2, size // 2), size // 4, (255, 255, 255), -1)
    return img


def stitch_side_by_side(left, right, overlap=30):
    h, w = left.shape[:2]
    canvas_w = w + right.shape[1] - overlap
    canvas = np.zeros((h, canvas_w, 3), dtype=np.uint8)
    canvas[:, :w] = left

    homography = np.array([[1, 0, w - overlap], [0, 1, 0], [0, 0, 1]], dtype=np.float64)
    warped_right = cv2.warpPerspective(right, homography, (canvas_w, h))

    mask = (warped_right.sum(axis=2) > 0)
    blended = canvas.copy()
    blended[mask] = warped_right[mask]
    return blended


if __name__ == "__main__":
    left = make_tile((180, 60, 60))
    right = make_tile((60, 60, 180))

    result = stitch_side_by_side(left, right)
    print("Left tile shape:", left.shape)
    print("Right tile shape:", right.shape)
    print("Stitched result shape:", result.shape)
    print("Mean pixel value:", round(float(result.mean()), 2))
