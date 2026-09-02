"""OpenCV Practice: cv2.applyColorMap on a Synthetic Intensity Map"""

import cv2
import numpy as np


def make_intensity_map(size=100):
    ys, xs = np.mgrid[0:size, 0:size]
    cx, cy = size / 2, size / 2
    dist = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)
    normalized = 255 - np.clip(dist / dist.max() * 255, 0, 255)
    return normalized.astype(np.uint8)


if __name__ == "__main__":
    intensity = make_intensity_map()
    heatmap = cv2.applyColorMap(intensity, cv2.COLORMAP_JET)

    print("Intensity map shape:", intensity.shape)
    print("Heatmap shape:", heatmap.shape)
    print("Hottest pixel (center) color:", heatmap[50, 50].tolist())
    print("Coolest pixel (corner) color:", heatmap[0, 0].tolist())
