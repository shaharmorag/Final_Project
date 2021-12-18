import cv2

file = "ISSshort.mp4"
capture = cv2.VideoCapture(file)

tracker = cv2.TrackerCSRT_create()
success, image = capture.read()

bbox = cv2.selectROI("Tracking", image, False)
tracker.init(image, bbox)

def deawBox(image, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(image, (x, y), ((x+w), (y+h)), (225, 0, 225), 3, 1)


while True:
    success, image = capture.read()
    success, bbox = tracker.update(image)
    print(bbox)
    if success:
        deawBox(image, bbox)
    else:
        pass

    cv2.imshow("Tracking", image)
    key = cv2.waitKey(1)

    if key == 27:
        break

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
