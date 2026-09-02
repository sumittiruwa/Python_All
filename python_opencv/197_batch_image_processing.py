"""OpenCV Practice: Apply an Operation over a Batch (List) of Synthetic Images"""

import cv2
import numpy as np


def make_batch(count=5, size=50, seed=0):
    rng = np.random.default_rng(seed)
    batch = []
    for i in range(count):
        color = tuple(int(v) for v in rng.integers(0, 256, size=3))
        img = np.full((size, size, 3), color, dtype=np.uint8)
        batch.append(img)
    return batch


def batch_grayscale_mean(batch):
    means = []
    for img in batch:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        means.append(float(gray.mean()))
    return means


if __name__ == "__main__":
    batch = make_batch()
    means = batch_grayscale_mean(batch)

    print("Batch size:", len(batch))
    print("Image shape:", batch[0].shape)
    for i, m in enumerate(means):
        print(f"Image {i}: grayscale mean={round(m, 2)}")
    print("Overall batch mean:", round(sum(means) / len(means), 2))
