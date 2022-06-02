from tkinter import *

top = Tk()

canvas_width = 800
canvas_height = 400

top.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(top, width=canvas_width, height=canvas_height)
can_widget.pack()

## The line goes from the point x1, y1 to x2, y2
can_widget.create_line(0,0,800,400, fill="red") 
can_widget.create_line(800,0,0,400, fill="red") 

## To create a rectangle specify parameters in this order - coors of top left and coors of bottom right
can_widget.create_rectangle(3,5,700,300,fill='red')

can_widget.create_text(200, 200, text="python")

can_widget.create_oval(344,233,244,355)



top.mainloop()