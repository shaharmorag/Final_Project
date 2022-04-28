from tkinter import *
from tracker import tracking

top = Tk()
top.title("Tracking Control")
top.geometry("270x280")
top['bg'] = '#0fadff'
# my_label = Label(top, text="satellite").pack()
# my_label.pack()
# my_label.grid(row=0, columm=0)


def my_button():
    label1 = Label(top, text="Detecting object")
    label1.pack()


def start():
    tracking(0.4, -100, 0.5, 30)

def azimuth(number):
    pass

# my_button = Button(top, text="start simulation", padx=20, pady=20, command=my_button)
# my_button.pack()
input_label = Label(top, text="Insert detection values:", bg='#0fadff').place(x=50, y=20)
scale_label = Label(top, text="Scale", bg='#0fadff').place(x=50, y=45)
scale_input = Entry(top, width=10).place(x=110, y=45)
density_label = Label(top, text="Density", bg='#0fadff').place(x=50, y=70)
density_input = Entry(top, width=10).place(x=110, y=70)
angle_label = Label(top, text="Angle", bg='#0fadff').place(x=50, y=95)
angle_input = Entry(top, width=10).place(x=110, y=95)

start_button = Button(top, text="Start", padx=20, command=start).place(x=50, y=130)

azimuth_label = Label(top, text="Azimuth", bg='#0fadff').place(x=50, y=170)
azimuth_input = Entry(top, width=10).place(x=110, y=170)
elevation_label = Label(top, text="Elevation", bg='#0fadff').place(x=50, y=195)
elevation_input = Entry(top, width=10).place(x=110, y=195)

export_button = Button(top, text="Export Data", padx=20).place(x=50, y=230)

top.mainloop()
