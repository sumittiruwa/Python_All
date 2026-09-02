"""OpenCV Practice: Camera Matrix Intrinsics and projectPoints"""

import cv2
import numpy as np


def build_camera_matrix(fx=800.0, fy=800.0, cx=320.0, cy=240.0):
    return np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]], dtype=np.float64)


def make_object_points():
    return np.array([[0, 0, 5], [1, 0, 5], [0, 1, 5], [1, 1, 5], [0.5, 0.5, 8]], dtype=np.float64)


if __name__ == "__main__":
    camera_matrix = build_camera_matrix()
    rvec = np.zeros((3, 1))
    tvec = np.zeros((3, 1))
    dist = np.zeros((5, 1))

    object_points = make_object_points()
    image_points, _ = cv2.projectPoints(object_points, rvec, tvec, camera_matrix, dist)
    image_points = image_points.reshape(-1, 2)

    print("Camera matrix:\n", camera_matrix)
    print("3D points:\n", object_points)
    print("Projected 2D points:\n", np.round(image_points, 2))
