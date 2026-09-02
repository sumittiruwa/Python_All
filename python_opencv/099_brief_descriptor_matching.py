"""OpenCV Practice: Binary Descriptor Matching (ORB descriptors, BRIEF-style)"""

import cv2
import numpy as np


def make_pair_of_images(size=100, shift=5, seed=6):
    base = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(base, (20, 20), (60, 60), 220, -1)
    cv2.circle(base, (75, 75), 12, 180, -1)
    rng = np.random.default_rng(seed)
    noise = rng.integers(0, 15, base.shape, dtype=np.uint8)
    img1 = cv2.add(base, noise)

    shifted = np.zeros_like(base)
    shifted[:, shift:] = base[:, : size - shift]
    img2 = cv2.add(shifted, noise)
    return img1, img2


def match_descriptors(img1, img2):
    orb = cv2.ORB_create(nfeatures=100)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    if des1 is None or des2 is None:
        return [], kp1, kp2

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(des1, des2)
    matches = sorted(matches, key=lambda m: m.distance)
    return matches, kp1, kp2


if __name__ == "__main__":
    img1, img2 = make_pair_of_images()
    matches, kp1, kp2 = match_descriptors(img1, img2)

    print("Keypoints img1:", len(kp1), "img2:", len(kp2))
    print("Matches found:", len(matches))
    for m in matches[:5]:
        print(f"queryIdx={m.queryIdx}, trainIdx={m.trainIdx}, distance={m.distance}")
