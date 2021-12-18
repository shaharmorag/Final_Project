import cv2

filename = "C://Users//shaha//Downloads//zoom_0.mp4"
capture = cv2.VideoCapture(filename)

# tracker = cv2.TrackerMOSSE_create()
tracker2 = cv2.TrackerCSRT_create()
success, image = capture.read()

bbox = cv2.selectROI("Tracking", image, False)
tracker2.init(image, bbox)

while True:
    success, image = capture.read()
    cv2.imshow("Tracking", image)






    if cv2.waitKey(1) & 0xff == ord('q'):
        break



