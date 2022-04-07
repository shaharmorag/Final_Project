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

def get_line(image2):

    # Read gray image
    ###image = cv2.imread(image, 0)

    # Create default parametrization LSD
    lsd = cv2.createLineSegmentDetector(0)
    # image = image.resize((360, 360))
    # Detect lines in the image
    image = list(image2)
    mat = np.zeros((1096,1936))
    for i in range(1096):
        for j in range(1936):
            mat[i][j] = (image[i][j][0]).astype(int)
    mat = mat.astype(np.uint8)
    lines = lsd.detect(mat)[0]  # Position 0 of the returned tuple are the detected lines
    print(lines)
    dominant_line_index = find_longest_line(lines)
    x_coord = int(lines[dominant_line_index][0][0])
    y_coord = int(lines[dominant_line_index][0][1])
    w = int(abs(lines[dominant_line_index][0][0] - lines[dominant_line_index][0][2]))
    h = int(abs(lines[dominant_line_index][0][1] - lines[dominant_line_index][0][3]))

    # Draw detected lines in the image
    drawn_img = lsd.drawSegments(mat, lines[dominant_line_index])

    # Show image
    #cv2.imshow("LSD", drawn_img)
    cv2.waitKey(0)

    # set size for the box
    print(f"detection coordinates: {x_coord}, {y_coord}, {w}, {h}")
    return(x_coord, y_coord, w + 10, h + 10)

#get_line("large line.png")