"""OpenCV Practice: cv2.rotatedRectangleIntersection"""

import cv2


def make_rects():
    rect1 = ((50, 50), (60, 30), 0)
    rect2 = ((70, 60), (60, 30), 45)
    return rect1, rect2


def intersect(rect1, rect2):
    status, points = cv2.rotatedRectangleIntersection(rect1, rect2)
    area = cv2.contourArea(points) if points is not None else 0.0
    return status, area


STATUS_NAMES = {0: "no intersection", 1: "full intersection", 2: "partial intersection"}


if __name__ == "__main__":
    rect1, rect2 = make_rects()
    status, area = intersect(rect1, rect2)

    print("Rect1:", rect1)
    print("Rect2:", rect2)
    print("Status:", STATUS_NAMES.get(status, status))
    print("Intersection area:", round(area, 2))
