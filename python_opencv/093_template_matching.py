"""OpenCV Practice: Template Matching"""

import cv2
import numpy as np


def make_scene_and_template(size=100):
    scene = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(scene, (60, 40), (85, 65), 200, -1)
    template = scene[40:65, 60:85].copy()
    return scene, template


def match_template(scene, template):
    result = cv2.matchTemplate(scene, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    return max_val, max_loc


if __name__ == "__main__":
    scene, template = make_scene_and_template()
    max_val, max_loc = match_template(scene, template)

    print("Template shape:", template.shape)
    print("Best match score:", round(float(max_val), 4))
    print("Best match top-left location:", max_loc)
    print("Expected location:", (60, 40))
