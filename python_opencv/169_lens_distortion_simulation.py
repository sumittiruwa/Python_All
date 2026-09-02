"""OpenCV Practice: Apply Synthetic Radial Lens Distortion via remap"""

import cv2
import numpy as np


def make_grid_image(size=200, step=20):
    img = np.full((size, size, 3), 20, dtype=np.uint8)
    for v in range(0, size, step):
        cv2.line(img, (v, 0), (v, size), (255, 255, 255), 1)
        cv2.line(img, (0, v), (size, v), (255, 255, 255), 1)
    return img


def radial_distortion_maps(size, strength=0.0000015):
    cx, cy = size / 2, size / 2
    ys, xs = np.mgrid[0:size, 0:size].astype(np.float32)
    dx, dy = xs - cx, ys - cy
    r2 = dx ** 2 + dy ** 2
    factor = 1 + strength * r2
    map_x = cx + dx * factor
    map_y = cy + dy * factor
    return map_x.astype(np.float32), map_y.astype(np.float32)


if __name__ == "__main__":
    img = make_grid_image()
    map_x, map_y = radial_distortion_maps(img.shape[0])
    distorted = cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR)

    print("Image shape:", img.shape)
    print("Map shapes:", map_x.shape, map_y.shape)
    print("Distorted mean pixel value:", round(float(distorted.mean()), 2))
