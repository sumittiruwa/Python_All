#only for camera permission
import cv2
# video_cap = cv2.VideoCapture(0)
# while True:
#     ret , video_da = video_cap.read()
#     cv2.imshow("Video", video_da)
#     if cv2.waitKey(10) == ord("a"):
#         break
# video_cap.release()
# cv2.destroyAllWindows()


#face detection
face_cap = cv2.CascadeClassifier("C:/Users/Sumit/AppData/Local/Programs/Python/Python314/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")  # capture the nose, eyes and parts of the faec
video_cap = cv2.VideoCapture(0)
while True:
    ret , video_da = video_cap.read()
    col = cv2.cvtColor(video_da, cv2.COLOR_BGR2GRAY)  # convert the video to gray scale
    faces = face_cap.detectMultiScale(col, 1.3, 5)
    cv2.imshow("Video", video_da)
    for (x,y,w,h) in faces:
        cv2.rectangle(video_da, (x,y), (x+w, y+h), (0,255,0), 2)  # draw a rectangle around the face


    cv2.imshow("Video", video_da)
    if cv2.waitKey(10) == ord("a"):
        break
video_cap.release()
cv2.destroyAllWindows()