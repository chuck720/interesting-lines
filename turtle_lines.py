from turtle import *
from tkinter import *

root = Tk()

canvas_y_entry = Entry(root, width = 50)
canvas_y_entry.insert(0, "How tall would you like the canvas? (pixals)")
canvas_y_entry.pack()

canvas_x_entry = Entry(root, width = 50)
canvas_x_entry.insert(0, "How wide should the drawing be? (pixals)")
canvas_x_entry.pack()

canvas_spacing_entry = Entry(root, width = 50)
canvas_spacing_entry.insert(0, "spacing? (larger number = more lines)")
canvas_spacing_entry.pack()

canvas_speed_entry = Entry(root, width = 50)
canvas_speed_entry.insert(0, "how fast do you want to draw? (0 - 10, 0 is fastest)")
canvas_speed_entry.pack()

def draw_mandala():

    canvas_x = int(canvas_x_entry.get())
    canvas_y = int(canvas_y_entry.get())
    spacing = int(canvas_spacing_entry.get())
    turtle_speed = int(canvas_speed_entry.get())
    dist_x = canvas_x / spacing
    dist_y = canvas_y / spacing
    speed(turtle_speed)

    i = 0
    while i < spacing:
        penup()
        forward(dist_x)
        pendown()
        goto(0, canvas_y - i * dist_y)
        goto(-dist_x - i * dist_x, 0)
        goto(0, -canvas_y + i * dist_y)
        goto(dist_x + i * dist_x, 0)
        i += 1

    goto(-canvas_x, 0)
    penup()
    goto(0, -canvas_y)
    pendown()
    goto(0, canvas_y)
    penup()
    goto(0, 0)

def clear_screen():
    clear()

create_button = Button(root, text = "create", command = draw_mandala)
create_button.pack()
clear_button = Button(root, text = "clear", command = clear_screen)
clear_button.pack()

mainloop()

root.mainloop()