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
    print(f"the longest line index: {index}\n")
    return index

def get_line(image2):

    # Read gray image
    ###image = cv2.imread(image, 0)

    # Create default parametrization LSD
    lsd = cv2.createLineSegmentDetector(2, scale=None, log_eps=None, density_th=None, ang_th=None) # density_th[0,1]: 0 most sensitive, ang_th: bigger angle more curved lines,

    # Detect lines in the image
    image = list(image2)
    mat = np.zeros((image2.shape[0], image2.shape[1]))

    for i in range(image2.shape[0]):
        for j in range(image2.shape[1]):
            mat[i][j] = (image[i][j][0]).astype(int)
    mat = mat.astype(np.uint8)

    lines = lsd.detect(mat)[0]  # Position 0 of the returned tuple are the detected lines
    dominant_line_index = find_longest_line(lines)
    x_coord = min(int(lines[dominant_line_index][0][0]), int(lines[dominant_line_index][0][2]))
    y_coord = min(int(lines[dominant_line_index][0][1]), int(lines[dominant_line_index][0][3]))
    w = int(abs(lines[dominant_line_index][0][0] - lines[dominant_line_index][0][2]))
    if w < 10:
        w += 15
    h = int(abs(lines[dominant_line_index][0][1] - lines[dominant_line_index][0][3]))
    if h < 10:
        h += 15

    # Draw detected lines in the image
    drawn_img = lsd.drawSegments(mat, lines[dominant_line_index])
    # drawn_img = lsd.drawSegments(mat, lines[:])

    # Show image
    cv2.imshow("LSD", drawn_img)
    cv2.waitKey(0)

    print(f"detection coordinates: {x_coord}, {y_coord}, {w}, {h}\n")
    return(x_coord, y_coord, w+20, h+20)

#get_line("large line.png")