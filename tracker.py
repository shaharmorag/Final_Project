import cv2
# from image_diff import run_image_diff
from lines import get_line
from tkinter import *
import pandas as pd
import openpyxl
import numpy as np


def export(tracking_data):
    # list1 = [10, 20, 30, 40]
    # list2 = [40, 30, 20, 10]
    col1 = "X"
    col2 = "Y"
    col3 = "W"
    col4 = "H"
    print("exporting to exel")
    # data = pd.DataFrame({col1: list1, col2: list2})
    # data = pd.DataFrame({col1: tracking_data})
    # data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)


def draw_box(image, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(image, (x, y), ((x + w), (y + h)), (225, 0, 225), 3, 1)


def detection(scale, log_eps, density_th, ang_th):
    file = "bright_line_slow_tracking2.mp4"
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
    bbox = get_line(frame1, scale, log_eps, density_th, ang_th)
    tracker.init(frame1, bbox)
    return capture, tracker


def loop(capture, tracker):
    tracking_data = np.zeros((500, 4))
    index = 0
    while True:
        success, image = capture.read()
        success, bbox = tracker.update(image)
        tracking_data[index] = bbox

        if success:
            draw_box(image, bbox)
            print(bbox)
        else:
            pass
        cv2.imshow("Tracking", image)
        key = cv2.waitKey(1)

        if key == 27:
            export(tracking_data)
            break

        if cv2.waitKey(1) & 0xff == ord('q'):
            export(tracking_data)
            break

        index += 1





top = Tk()
top.title("Tracking Control")
top.geometry("270x280")
top['bg'] = '#0fadff'


def my_button():
    label1 = Label(top, text="Detecting object")
    label1.pack()


def start():

    start_button.config(state=DISABLED)
    detection(0.4, -100, 0.5, 30)
    # detection(float(scale_input.get()), -100, float(density_input.get()), float(angle_input.get()))

    print("hi there")


def azimuth(number):
    pass

# my_button = Button(top, text="start simulation", padx=20, pady=20, command=my_button)
# my_button.pack()
input_label = Label(top, text="Insert detection values:", bg='#0fadff').place(x=50, y=20)
scale_label = Label(top, text="Scale", bg='#0fadff').place(x=50, y=45)
scale_input = Entry(top, width=10)
scale_input.place(x=110, y=45)
density_label = Label(top, text="Density", bg='#0fadff').place(x=50, y=70)
density_input = Entry(top, width=10)
density_input.place(x=110, y=70)
angle_label = Label(top, text="Angle", bg='#0fadff').place(x=50, y=95)
angle_input = Entry(top, width=10)
angle_input.place(x=110, y=95)

global start_button
start_button = Button(top, text="Start", padx=20, command=start)
start_button.place(x=50, y=130)

azimuth_label = Label(top, text="Azimuth", bg='#0fadff').place(x=50, y=170)
azimuth_input = Entry(top, width=10).place(x=110, y=170)
elevation_label = Label(top, text="Elevation", bg='#0fadff').place(x=50, y=195)
elevation_input = Entry(top, width=10).place(x=110, y=195)

export_button = Button(top, text="Export Data", padx=20).place(x=50, y=230)

# top.mainloop()

# export data to exel



def main():
    capture, tracker = detection(0.4, -100, 0.5, 30)
    loop(capture, tracker)

if __name__ == '__main__':
    main()
