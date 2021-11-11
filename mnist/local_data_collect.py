from tkinter import *

class DataCollect:

    def __init__(self, stroke_width):
        self.stroke_width = stroke_width
        self.last_x = 0
        self.last_y = 0
        self.canvas = None

    def get_xy(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw_stroke(self, event):    
        self.canvas.create_oval(
            (self.last_x - self.stroke_width,
             self.last_y - self.stroke_width, 
            self.last_x + self.stroke_width, 
            self.last_y + self.stroke_width),
            fill='white', outline = 'white')
        self.last_x, self.last_y = event.x, event.y

    def on_mouse_right_button(self, event):
        print("pressed", event.keysym)

    def run(self):
        app = Tk()
        app.geometry("400x400")

        self.canvas = Canvas(app, bg='black')
        self.canvas.pack(anchor='nw', fill='both', expand=1)

        self.canvas.bind("<Button-1>", self.get_xy)
        # Button-3 corresponds to the right mouse button,
        # while Button-2 corresponds to the middle button if available,
        # that might be confusing if not reading the docs of tkinter.
        self.canvas.bind("<Button-3>", self.on_mouse_right_button)
        self.canvas.bind("<B1-Motion>", self.draw_stroke)

        app.mainloop()

dc = DataCollect(stroke_width=16)
dc.run()