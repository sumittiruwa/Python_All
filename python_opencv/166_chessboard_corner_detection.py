"""OpenCV Practice: findChessboardCorners on a Synthetic Chessboard"""

import cv2
import numpy as np


def make_chessboard(rows=6, cols=9, cell=30, margin=30):
    h = rows * cell + 2 * margin
    w = cols * cell + 2 * margin
    img = np.full((h, w), 255, dtype=np.uint8)
    for r in range(rows):
        for c in range(cols):
            if (r + c) % 2 == 0:
                y0, x0 = margin + r * cell, margin + c * cell
                cv2.rectangle(img, (x0, y0), (x0 + cell, y0 + cell), 0, -1)
    return img


def find_inner_corners(board_img, inner_rows=5, inner_cols=8):
    found, corners = cv2.findChessboardCorners(board_img, (inner_cols, inner_rows))
    return found, corners


if __name__ == "__main__":
    board = make_chessboard()
    found, corners = find_inner_corners(board)

    print("Board shape:", board.shape)
    print("Corners found:", found)
    if found:
        print("Corner count:", len(corners))
        print("First corner:", np.round(corners[0].ravel(), 2))
