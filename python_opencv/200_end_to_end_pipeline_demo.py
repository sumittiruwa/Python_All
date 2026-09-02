"""OpenCV Practice: End-to-End Pipeline (synth -> gray -> blur -> edges -> contours)"""

import cv2
import numpy as np


def make_scene(size=200, seed=0):
    rng = np.random.default_rng(seed)
    img = np.full((size, size, 3), (30, 30, 30), dtype=np.uint8)
    cv2.rectangle(img, (30, 30), (90, 90), (0, 200, 0), -1)
    cv2.circle(img, (150, 140), 35, (0, 0, 220), -1)
    noise = rng.normal(0, 5, img.shape)
    return np.clip(img.astype(np.float32) + noise, 0, 255).astype(np.uint8)


def run_pipeline(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    return gray, blurred, edges, contours


if __name__ == "__main__":
    scene = make_scene()
    gray, blurred, edges, contours = run_pipeline(scene)

    areas = sorted((round(cv2.contourArea(c), 1) for c in contours), reverse=True)[:3]

    print("Scene shape:", scene.shape)
    print("Gray shape:", gray.shape)
    print("Blurred mean:", round(float(blurred.mean()), 2))
    print("Edge pixel count:", int((edges > 0).sum()))
    print("Contours found:", len(contours))
    print("Top-3 contour areas:", areas)
