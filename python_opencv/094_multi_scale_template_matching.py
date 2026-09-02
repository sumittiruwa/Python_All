"""OpenCV Practice: Multi-Scale Template Matching"""

import cv2
import numpy as np


def make_scene_and_template(size=150):
    scene = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(scene, (40, 30), (70, 60), 220, -1)
    template = np.zeros((20, 20), dtype=np.uint8)
    cv2.rectangle(template, (0, 0), (19, 19), 220, -1)
    return scene, template


def multi_scale_match(scene, template, scales=(0.5, 1.0, 1.5, 2.0)):
    best = None
    for scale in scales:
        w = max(8, int(template.shape[1] * scale))
        h = max(8, int(template.shape[0] * scale))
        if w >= scene.shape[1] or h >= scene.shape[0]:
            continue
        resized = cv2.resize(template, (w, h))
        result = cv2.matchTemplate(scene, resized, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if best is None or max_val > best[0]:
            best = (max_val, max_loc, scale)
    return best


if __name__ == "__main__":
    scene, template = make_scene_and_template()
    best_val, best_loc, best_scale = multi_scale_match(scene, template)

    print("Best scale:", best_scale)
    print("Best match score:", round(float(best_val), 4))
    print("Best match location:", best_loc)
