"""OpenCV Practice: Build a Collage with Borders from Synthetic Tiles"""

import cv2
import numpy as np


def make_tiles(count=4, size=50):
    colors = [(180, 40, 40), (40, 180, 40), (40, 40, 180), (180, 180, 40)]
    return [np.full((size, size, 3), colors[i], dtype=np.uint8) for i in range(count)]


def add_border(tile, thickness=4, color=(255, 255, 255)):
    return cv2.copyMakeBorder(tile, thickness, thickness, thickness, thickness, cv2.BORDER_CONSTANT, value=color)


def build_collage(tiles, cols=2, border=4):
    bordered = [add_border(t, border) for t in tiles]
    rows = (len(bordered) + cols - 1) // cols
    h, w = bordered[0].shape[:2]
    collage = np.full((rows * h, cols * w, 3), 30, dtype=np.uint8)
    for idx, tile in enumerate(bordered):
        r, c = divmod(idx, cols)
        collage[r * h:(r + 1) * h, c * w:(c + 1) * w] = tile
    return collage


if __name__ == "__main__":
    tiles = make_tiles()
    collage = build_collage(tiles, cols=2, border=5)

    print("Tile count:", len(tiles))
    print("Bordered tile shape:", add_border(tiles[0], 5).shape)
    print("Collage shape:", collage.shape)
