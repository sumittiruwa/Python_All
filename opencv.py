import cv2
import numpy as np
import datetime
import os

# -----------------------------
# Create folders
# -----------------------------
os.makedirs("captures", exist_ok=True)
os.makedirs("recordings", exist_ok=True)

# -----------------------------
# Webcam
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam.")
    exit()

# -----------------------------
# Variables
# -----------------------------
background = None
recording = False
writer = None

font = cv2.FONT_HERSHEY_SIMPLEX

print("===================================")
print("   MOTION SECURITY CAMERA")
print("===================================")
print("Press Q = Quit")
print("Press S = Save Screenshot")
print("Press R = Reset Background")
print("===================================")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (900, 600))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # First frame becomes background
    if background is None:
        background = gray.copy().astype("float")
        continue

    # Update background slowly
    cv2.accumulateWeighted(gray, background, 0.01)

    diff = cv2.absdiff(gray, cv2.convertScaleAbs(background))

    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

    thresh = cv2.dilate(thresh, None, iterations=3)

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    motion = False

    for contour in contours:

        if cv2.contourArea(contour) < 1500:
            continue

        motion = True

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Motion",
            (x, y - 10),
            font,
            0.7,
            (0, 255, 0),
            2
        )

    # Current time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cv2.putText(
        frame,
        now,
        (10, 30),
        font,
        0.7,
        (255, 255, 255),
        2
    )

    # Recording
    if motion:

        cv2.putText(
            frame,
            "STATUS : MOTION DETECTED",
            (10, 70),
            font,
            0.8,
            (0, 0, 255),
            2
        )

        if not recording:

            filename = datetime.datetime.now().strftime(
                "recordings/%Y%m%d_%H%M%S.avi"
            )

            fourcc = cv2.VideoWriter_fourcc(*"XVID")

            writer = cv2.VideoWriter(
                filename,
                fourcc,
                20,
                (900, 600)
            )

            recording = True

        writer.write(frame)

    else:

        cv2.putText(
            frame,
            "STATUS : SAFE",
            (10, 70),
            font,
            0.8,
            (0, 255, 0),
            2
        )

        if recording:

            writer.release()

            writer = None

            recording = False

    cv2.imshow("Security Camera", frame)

    cv2.imshow("Threshold", thresh)

    key = cv2.waitKey(1) & 0xFF

    # Quit
    if key == ord("q"):
        break

    # Screenshot
    elif key == ord("s"):

        filename = datetime.datetime.now().strftime(
            "captures/%Y%m%d_%H%M%S.jpg"
        )

        cv2.imwrite(filename, frame)

        print("Screenshot saved:", filename)

    # Reset background
    elif key == ord("r"):

        background = gray.copy().astype("float")

        print("Background reset.")

# Cleanup
if writer is not None:
    writer.release()

cap.release()
cv2.destroyAllWindows()