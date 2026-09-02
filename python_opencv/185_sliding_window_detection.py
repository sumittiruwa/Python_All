"""OpenCV Practice: Slide a Window over an Image, Score Each Position"""

import cv2
import numpy as np


def make_image_with_bright_spot(size=100):
    img = np.full((size, size), 30, dtype=np.uint8)
    cv2.rectangle(img, (60, 60), (85, 85), 220, -1)
    return img


def sliding_window_scores(img, win_size=20, stride=10):
    scores = []
    h, w = img.shape
    for y in range(0, h - win_size + 1, stride):
        for x in range(0, w - win_size + 1, stride):
            window = img[y:y + win_size, x:x + win_size]
            scores.append(((x, y), float(window.mean())))
    return scores


if __name__ == "__main__":
    img = make_image_with_bright_spot()
    scores = sliding_window_scores(img)

    best_pos, best_score = max(scores, key=lambda item: item[1])
    print("Image shape:", img.shape)
    print("Windows scanned:", len(scores))
    print("Best window position:", best_pos)
    print("Best window mean intensity:", round(best_score, 2))
