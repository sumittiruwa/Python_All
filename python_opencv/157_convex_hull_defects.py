"""OpenCV Practice: Convex Hull and Convexity Defects"""

import cv2
import numpy as np


def make_star_image(size=200):
    img = np.zeros((size, size), dtype=np.uint8)
    center = (size // 2, size // 2)
    outer, inner, n_points = 90, 35, 5
    pts = []
    for i in range(n_points * 2):
        angle = i * np.pi / n_points - np.pi / 2
        r = outer if i % 2 == 0 else inner
        pts.append((center[0] + r * np.cos(angle), center[1] + r * np.sin(angle)))
    pts = np.array(pts, dtype=np.int32)
    cv2.fillPoly(img, [pts], 255)
    return img


def hull_and_defects(binary_img):
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=cv2.contourArea)
    hull_indices = cv2.convexHull(contour, returnPoints=False)
    hull_indices = np.sort(hull_indices, axis=0)
    defects = cv2.convexityDefects(contour, hull_indices)
    return contour, hull_indices, defects


if __name__ == "__main__":
    img = make_star_image()
    contour, hull_indices, defects = hull_and_defects(img)

    print("Contour points:", len(contour))
    print("Hull vertices:", len(hull_indices))
    print("Convexity defects found:", 0 if defects is None else len(defects))
    if defects is not None:
        depths = defects.reshape(-1, 4)[:, 3]
        deepest = depths.max() / 256.0
        print("Deepest defect depth:", round(float(deepest), 2))
