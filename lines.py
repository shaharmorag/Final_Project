import cv2
import numpy as np

def find_longest_line(lines):
    x = 0
    y = 0
    index = -1
    for line in range(len(lines) - 1):
        current_x = abs(lines[line][0][0] - lines[line][0][2])
        current_y = abs(lines[line][0][1] - lines[line][0][3])
        if current_x > x:
            x = current_x
            index_x = line
        if current_y > y:
            y = current_y
            index_y = line
    if x > y:
        index = index_x
    else:
        index = index_y
    print(f"the longest line index: {index}")
    return index

def get_line(image):

    # Read gray image
    img = cv2.imread(image, 0)

    # Create default parametrization LSD
    lsd = cv2.createLineSegmentDetector(0)

    # Detect lines in the image
    lines = lsd.detect(img)[0]  # Position 0 of the returned tuple are the detected lines
    print(lines)
    dominant_line_index = find_longest_line(lines)

    # Draw detected lines in the image
    drawn_img = lsd.drawSegments(img, lines[dominant_line_index])

    # Show image
    cv2.imshow("LSD", drawn_img)
    cv2.waitKey(0)

get_line("eye.jpeg")