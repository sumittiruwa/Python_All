"""OpenCV Practice: Feature Matching with BFMatcher knnMatch and Ratio Test"""

import cv2
import numpy as np


def make_pair_of_images(size=120, seed=7):
    base = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(base, (15, 15), (55, 55), 210, -1)
    cv2.circle(base, (85, 85), 15, 170, -1)
    cv2.rectangle(base, (70, 15), (100, 45), 140, -1)
    rng = np.random.default_rng(seed)
    noise = rng.integers(0, 10, base.shape, dtype=np.uint8)
    img1 = cv2.add(base, noise)
    img2 = cv2.add(base, rng.integers(0, 10, base.shape, dtype=np.uint8))
    return img1, img2


def knn_match_with_ratio_test(img1, img2, ratio=0.75):
    orb = cv2.ORB_create(nfeatures=150)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    if des1 is None or des2 is None:
        return [], kp1, kp2

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    knn_matches = matcher.knnMatch(des1, des2, k=2)

    good = []
    for pair in knn_matches:
        if len(pair) == 2:
            m, n = pair
            if m.distance < ratio * n.distance:
                good.append(m)
    return good, kp1, kp2


if __name__ == "__main__":
    img1, img2 = make_pair_of_images()
    good_matches, kp1, kp2 = knn_match_with_ratio_test(img1, img2)

    print("Keypoints img1:", len(kp1), "img2:", len(kp2))
    print("Good matches after ratio test:", len(good_matches))
    for m in good_matches[:5]:
        print(f"queryIdx={m.queryIdx}, trainIdx={m.trainIdx}, distance={round(m.distance,2)}")
