from skimage.metrics import structural_similarity
import numpy as np
import imutils
import cv2

def set_images(img1, img2):
    # convert the images to grayscale
    grayA = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    return img1, img2, grayA, grayB


def compare(imageA, imageB, grayA, grayB):
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

    # threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour and then draw the
        # bounding box on both input images to represent where the two
        # images differ
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imwrite("diff_image.jpg", diff)

    return score, diff, thresh


def show_diff(imageA, imageB, diff, thresh):
    cv2.imshow("Original", imageA)
    cv2.imshow("Modified", imageB)
    cv2.imshow("Diff", diff)
    cv2.imshow("Thresh", thresh)
    cv2.waitKey(0)


def run_image_diff(img1, img2):
    # file = "ISSshort.mp4"
    # cap = cv2.VideoCapture(file)  # load a video
    # success, img1 = cap.read()  # to show a frame
    # success, img2 = cap.read()  # to show a frame

    imageA, imageB, grayA, grayB = set_images(img1, img2)

    score, diff, thresh = compare(imageA, imageB, grayA, grayB)
    # show_diff(imageA, imageB, diff, thresh)
    x, y = np.unravel_index(diff.argmin(), diff.shape)
    print(f"the indexes of the detection: {x}, {y}")
    return x, y


