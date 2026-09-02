"""OpenCV Practice: Minimum Enclosing Triangle"""

import cv2
import numpy as np


def make_polygon_points():
    return np.array([[50, 50], [150, 30], [180, 100], [140, 170], [60, 150], [20, 100]], dtype=np.int32)


def enclosing_triangle(points):
    area, triangle = cv2.minEnclosingTriangle(points)
    return area, triangle.reshape(-1, 2)


if __name__ == "__main__":
    points = make_polygon_points()
    area, triangle = enclosing_triangle(points)

    print("Input polygon points:", len(points))
    print("Triangle area:", round(float(area), 2))
    print("Triangle vertices:\n", np.round(triangle, 1))
