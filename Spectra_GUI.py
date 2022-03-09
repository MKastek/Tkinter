from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Get the newest widget themes from Tk 8.5
from tkinter import ttk

# Create the main window that holds all the widgets
from matplotlib.figure import Figure

root = Tk()



def replot(subplot):
    fig.clf()
    subplot = fig.add_subplot(111)
    subplot.plot([0,2,5],[1,-10,12])
    fig.canvas.draw_idle()

fig = Figure(figsize=(5, 4), dpi=100)
subplot = fig.add_subplot(111)
# Define the title for the window
root.title("Spectral data")

# The frame surrounds the interface with the widgets
# A frame is used so the widgets and background
# colors are consistent
# Define padding for left top and right bottom
top_frame = ttk.Frame(root, padding="10 10 10 10")
top_frame.pack(side=TOP)

data_button = Button(top_frame, text="Data",  command=lambda: replot(subplot),width=10, height=2)
lines_button = Button(top_frame, text="Lines", width=10, height=2)
data_button.pack(side=LEFT)
lines_button.pack(side=LEFT)

current_value = DoubleVar()
slider = Scale(top_frame,from_=0,to=1,orient='horizontal',variable=current_value, resolution=0.01)
slider.pack(side=LEFT)


y = np.arange(0, 3, .01)
x = np.arange(0, 3, .01)

subplot.plot(x, y)
canvas = FigureCanvasTkAgg(fig, master=root)

canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

root.mainloop()