"""OpenCV Practice: cv2.remap with a Custom Wave Mapping"""

import cv2
import numpy as np


def make_stripe_image(size=200, step=10):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    for x in range(0, size, step * 2):
        img[:, x:x + step] = (0, 200, 0)
    return img


def wave_maps(size, amplitude=8.0, frequency=0.05):
    ys, xs = np.mgrid[0:size, 0:size].astype(np.float32)
    map_x = xs + amplitude * np.sin(frequency * ys)
    map_y = ys.copy()
    return map_x, map_y


if __name__ == "__main__":
    img = make_stripe_image()
    map_x, map_y = wave_maps(img.shape[0])
    waved = cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

    print("Image shape:", img.shape)
    print("Original mean:", round(float(img.mean()), 2))
    print("Waved mean:", round(float(waved.mean()), 2))
    print("Pixels changed:", int(np.any(img != waved, axis=2).sum()))
