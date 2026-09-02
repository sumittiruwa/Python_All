"""OpenCV Practice: FAST Feature Detector"""

import cv2
import numpy as np


def make_checkerboard_like_image(size=100, step=20):
    img = np.zeros((size, size), dtype=np.uint8)
    for y in range(0, size, step):
        for x in range(0, size, step):
            if (x // step + y // step) % 2 == 0:
                img[y : y + step, x : x + step] = 255
    return img


def detect_fast_keypoints(img, threshold=30):
    fast = cv2.FastFeatureDetector_create(threshold=threshold)
    keypoints = fast.detect(img, None)
    return keypoints


if __name__ == "__main__":
    image = make_checkerboard_like_image()
    keypoints = detect_fast_keypoints(image)

    print("Keypoints detected:", len(keypoints))
    for kp in keypoints[:5]:
        print(f"pt=({round(kp.pt[0],1)},{round(kp.pt[1],1)}), response={round(kp.response,2)}")
