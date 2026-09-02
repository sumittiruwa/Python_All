"""OpenCV Practice: cv2.pointPolygonTest"""

import cv2
import numpy as np


def make_polygon():
    return np.array([[20, 20], [180, 20], [180, 180], [20, 180]], dtype=np.int32)


def classify_points(polygon, points):
    results = []
    for p in points:
        distance = cv2.pointPolygonTest(polygon, (float(p[0]), float(p[1])), True)
        results.append(round(float(distance), 2))
    return results


if __name__ == "__main__":
    polygon = make_polygon()
    test_points = [(100, 100), (10, 10), (20, 20), (179, 179)]

    distances = classify_points(polygon, test_points)
    for point, distance in zip(test_points, distances):
        location = "inside" if distance > 0 else "outside" if distance < 0 else "on edge"
        print(f"Point {point}: distance={distance} ({location})")
