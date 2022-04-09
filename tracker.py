import cv2
# from image_diff import run_image_diff
from lines import get_line


def draw_box(image, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(image, (x, y), ((x + w), (y + h)), (225, 0, 225), 3, 1)


def main():
    file = "vid_pale_line_1.mp4"
    capture = cv2.VideoCapture(file)

    tracker = cv2.TrackerCSRT_create()

    ##### find diff in frames
    # success, frame1 = capture.read()
    # success, frame2 = capture.read()
    # x_target, y_target = run_image_diff(frame1, frame2-400)
    ## x_target, y_target = 502, 1009 ## boundry problems.
    # w_target = 20
    # h_target = 20
    # bbox = cv2.selectROI("Tracking", frame2, False)
    # bbox = (int(x_target), int(y_target), w_target, h_target)

    success, frame1 = capture.read()
    print(type(frame1))
    bbox = get_line(frame1)
    tracker.init(frame1, bbox)

    while True:
        success, image = capture.read()
        success, bbox = tracker.update(image)

        if success:
            draw_box(image, bbox)
            print(bbox)
        else:
            pass
        cv2.imshow("Tracking", image)
        key = cv2.waitKey(1)

        if key == 27:
            break

        if cv2.waitKey(1) & 0xff == ord('q'):
            break


if __name__ == '__main__':
    main()
