"""OpenCV Practice: ORB Feature Detector and Descriptors"""

import cv2
import numpy as np


def make_textured_image(size=100, seed=5):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (45, 45), 200, -1)
    cv2.rectangle(img, (55, 55), (90, 90), 150, -1)
    rng = np.random.default_rng(seed)
    noise = rng.integers(0, 20, img.shape, dtype=np.uint8)
    return cv2.add(img, noise)


def detect_orb_features(img, n_features=50):
    orb = cv2.ORB_create(nfeatures=n_features)
    keypoints, descriptors = orb.detectAndCompute(img, None)
    return keypoints, descriptors


if __name__ == "__main__":
    image = make_textured_image()
    keypoints, descriptors = detect_orb_features(image)

    print("Keypoints detected:", len(keypoints))
    print("Descriptor shape:", None if descriptors is None else descriptors.shape)
    print("Descriptor dtype:", None if descriptors is None else descriptors.dtype)
