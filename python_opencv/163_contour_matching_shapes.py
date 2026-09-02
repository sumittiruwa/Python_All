"""OpenCV Practice: matchShapes to Compare Two Different Shapes"""

import cv2
import numpy as np


def contour_of(draw_fn, size=200):
    img = np.zeros((size, size), dtype=np.uint8)
    draw_fn(img)
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return max(contours, key=cv2.contourArea)


def draw_circle(img):
    cv2.circle(img, (100, 100), 60, 255, -1)


def draw_small_circle(img):
    cv2.circle(img, (100, 100), 55, 255, -1)


def draw_square(img):
    cv2.rectangle(img, (40, 40), (160, 160), 255, -1)


if __name__ == "__main__":
    circle_a = contour_of(draw_circle)
    circle_b = contour_of(draw_small_circle)
    square = contour_of(draw_square)

    circle_vs_circle = cv2.matchShapes(circle_a, circle_b, cv2.CONTOURS_MATCH_I1, 0.0)
    circle_vs_square = cv2.matchShapes(circle_a, square, cv2.CONTOURS_MATCH_I1, 0.0)

    print("Circle vs similar circle score:", round(circle_vs_circle, 5))
    print("Circle vs square score:", round(circle_vs_square, 5))
    print("More similar pair:", "circles" if circle_vs_circle < circle_vs_square else "square/circle")
