import cv2
import numpy as np
from object_detection import ObjectDetection

# init object_detection
od = ObjectDetection()

file = "19_29_32.avi"

cap = cv2.VideoCapture(file)  # load a video

while True:
    success, frame = cap.read()  # to show a frame
    if not success:
        break

    # detect object on frame
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes:
        (x, y, w, h) = box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:  # to be able to close the window on esc
        break

cap.release()
cv2.destroyAllWindows()