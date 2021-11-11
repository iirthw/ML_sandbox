from tkinter import *

from PIL import Image, ImageDraw

from colorutils import Color


# class ImageUtils:

#     @staticmethod
#     def get_pixels_of(canvas):
#         width = int(canvas["width"])
#         height = int(canvas["height"])
#         colors = []

#         for x in range(width):
#             column = []
#             for y in range(height):
#                 column.append(ImageUtils.get_pixel_color(canvas, x, y))
#             colors.append(column)

#         return colors

#     @staticmethod
#     def get_pixel_color(canvas, x, y):
#         ids = canvas.find_overlapping(x, y, x, y)

#         if len(ids) > 0:
#             index = ids[-1]
#             color = canvas.itemcget(index, "fill")
#             color = color.upper()
#             if color != '':
#                 print(color)
#                 return Color(color.upper())

#         return "lol"

class DataCollect:

    def __init__(self, stroke_width):
        self.stroke_width = stroke_width
        self.last_x = 0
        self.last_y = 0
        self.canvas = None

        # PIL image twin buffer that mirrors what is drawn on the canvas
        self.image_twin = None
        self.draw_twin = None

    def get_xy(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw_stroke(self, event):
        top_left_point = (
            self.last_x - self.stroke_width,
            self.last_y - self.stroke_width
            )
        bottom_right_point = (
            self.last_x + self.stroke_width, 
            self.last_y + self.stroke_width
            )

        # Draw on the canvas
        self.canvas.create_oval(
            (top_left_point[0],
            top_left_point[1], 
            bottom_right_point[0], 
            bottom_right_point[1]),
            fill='white', outline = 'white',
            )

        self.last_x, self.last_y = event.x, event.y

        # Draw on the image twin
        self.draw_twin.ellipse([top_left_point, bottom_right_point], fill='white')

    def on_mouse_right_button(self, event):
        # filename = 'temp.jpg'
        # self.imageTwin.save(f\ilename)
        pixel00 = self.image_twin.getpixel((0, 0))
        print(pixel00)

    def run(self):
        width = 100
        height = 100
        black = (0, 0, 0)
        self.image_twin = Image.new('RGB', (width, height), black)
        self.draw_twin = ImageDraw.Draw(self.image_twin)

        app = Tk()
        app.geometry("200x200")

        self.canvas = Canvas(app, bg='black')
        self.canvas.pack(anchor='nw', fill='both', expand=1)

        # img = ImageTk.PhotoImage(Image.open('black_tile.png'))
        # self.canvas.create_image(25,25, image=img, anchor=CENTER, tag = "lol")

        self.canvas.bind("<Button-1>", self.get_xy)
        # Button-3 corresponds to the right mouse button,
        # while Button-2 corresponds to the middle button if available,
        # that might be confusing if not reading the docs of tkinter.
        self.canvas.bind("<Button-3>", self.on_mouse_right_button)
        self.canvas.bind("<B1-Motion>", self.draw_stroke)

        app.mainloop()
 
dc = DataCollect(stroke_width=16)
dc.run()