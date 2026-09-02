"""OpenCV Practice: Tile Several Small Images into a Grid Mosaic"""

import cv2
import numpy as np


def make_tiles(count=6, size=40):
    colors = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (0, 200, 200), (200, 0, 200), (200, 200, 0)]
    tiles = []
    for i in range(count):
        tile = np.full((size, size, 3), colors[i % len(colors)], dtype=np.uint8)
        cv2.putText(tile, str(i), (8, size - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        tiles.append(tile)
    return tiles


def build_mosaic(tiles, cols):
    rows = (len(tiles) + cols - 1) // cols
    h, w = tiles[0].shape[:2]
    mosaic = np.zeros((rows * h, cols * w, 3), dtype=np.uint8)
    for idx, tile in enumerate(tiles):
        r, c = divmod(idx, cols)
        mosaic[r * h:(r + 1) * h, c * w:(c + 1) * w] = tile
    return mosaic


if __name__ == "__main__":
    tiles = make_tiles(count=6, size=40)
    mosaic = build_mosaic(tiles, cols=3)

    print("Tile count:", len(tiles))
    print("Tile shape:", tiles[0].shape)
    print("Mosaic shape:", mosaic.shape)
    print("Mosaic mean pixel value:", round(float(mosaic.mean()), 2))
