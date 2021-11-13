import os
import sys
import numpy as np
import math
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageDraw, ImageOps

class DataCollect:

    def __init__(self, stroke_size, canvas_width, canvas_height):
        self.stroke_size = stroke_size
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.last_x = 0
        self.last_y = 0
        self.canvas = None

        self.app = None

        # PIL image twin buffer that mirrors what is drawn on the canvas
        self.image_twin = None
        self.draw_twin = None

        # The twin image will be downscaled according to downscale_width and
        # downscale_height before adding that data to the pool for pickling.
        self.downscale_width = 16
        self.downscale_height = 16

        # constant used for on-demand increment and decrement of the stroke width.
        self.stroke_increment = 5
        self.stroke_min_size = 1
        self.stroke_max_size = max(self.canvas_width, self.canvas_height)

        # Current digit which is in use for the data collection
        self.curr_digit = 0

        # Data file: pickle data to that file
        self.data_file_name = 'data.pkl'
        # Actual data
        self.data = np.array([])

        # Constants for data sizes
        self.bytes_in_kb = 1024
        self.bytes_in_mb = 1024 * self.bytes_in_kb
        self.bytes_in_gb = 1024 * self.bytes_in_mb

        self.black = 0

    def get_xy(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw_stroke(self, event):
        top_left_point = (
            self.last_x - self.stroke_size,
            self.last_y - self.stroke_size
            )
        bottom_right_point = (
            self.last_x + self.stroke_size, 
            self.last_y + self.stroke_size
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

    def to_grayscale(self, image):
        return ImageOps.grayscale(image)

    def get_pixels(self):
        img = self.image_twin
        # img = self.to_grayscale(img)
        # thumbnail method can be used to downscale the image
        img.thumbnail((self.downscale_width, self.downscale_height), Image.ANTIALIAS)
        pix = list(img.getdata())
        pix = np.array(pix)
        pix = np.reshape(pix, (1, self.downscale_width, self.downscale_height))
        print(pix)
        return pix

    def on_mouse_right_button(self, event):
        # In case if a single pixel is needed, use the following: 
        # pixel00 = self.image_twin.getpixel((0, 0))
        
        pixels = list(self.image_twin.getdata())

        im = self.image_twin
        im.thumbnail((self.downscale_width, self.downscale_height), Image.ANTIALIAS)
        # plt.imshow(im)
        # plt.show()

        img_data = list(im.getdata())
        img_data = np.array(img_data)
        img_data = np.reshape(img_data, (self.downscale_width, self.downscale_height))
        print(img_data)
        # pix = np.array(1, img_data.getdata()).reshape(img_data.size[0], img_data.size[1], 1)
        # return pix

    def init_image_twin(self):
        self.image_twin = self.image_twin = Image.new('L', 
            (self.canvas_width, self.canvas_height), self.black)

    def clear_canvas(self, event):
        print('clear_canvas')
        # Clear Tk canvas
        self.canvas.delete('all')
        # Clear Pillow image as well 
        self.init_image_twin()
        self.draw_twin = ImageDraw.Draw(self.image_twin)

    def quit(self, event):
        self.app.quit()

    def decrement_stroke_size(self, event):
        temp = self.stroke_size - self.stroke_increment
        if temp < self.stroke_min_size:
            self.stroke_size = self.stroke_min_size
        else:
            self.stroke_size = temp
        
        print('decrement stroke size: ' + str(self.stroke_size))        

    def increment_stroke_size(self, event):
        temp = self.stroke_size + self.stroke_increment
        if temp > self.stroke_max_size:
            self.stroke_size = self.stroke_max_size
        else:
            self.stroke_size = temp
        
        print('increment stroke size: ' + str(self.stroke_size))

    def key_pressed(self, event):
        # Currently do not use match/case syntax (Python >= 3.10)
        # for the compatibility with Python <= 3.9
        cases = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6,
            '7' : 7, '8' : 8, '9' : 9}

        curr_digit = cases.get(event.keysym, -1)
        if curr_digit >= 0 and curr_digit <= 9:
            self.curr_digit = curr_digit
            print('Set current digit to : ' + str(self.curr_digit))

    def sizeof_data(self, data):
        num_bytes = sys.getsizeof(data)
        if num_bytes < self.bytes_in_kb:
            return str(num_bytes) + ' Bytes'
        elif num_bytes < self.bytes_in_mb:
            return str(math.floor(num_bytes / self.bytes_in_kb)) + ' KB'
        elif num_bytes < self.bytes_in_gb:
            return str(math.floor(num_bytes / self.bytes_in_mb)) + ' MB'
        else:
            return 'Data in use: over 1 GB..'

    def append_data(self, event):
        pix = self.get_pixels()
        pix[0] = self.curr_digit
        print(self.data.shape)

        if self.data.size > 0:
            self.data = np.append(self.data, pix, axis=0)
        else:
            self.data = pix

        print(self.data.shape)
        print(self.sizeof_data(self.data))

    def save_data(self, event):
        if os.path.isfile(self.data_file_name):
            print('lol')
        else:
            print('anti-lol')
            print(self.data.shape)

        # with file(self.data_file_name, 'wb') as data_file:

    def run(self):        
        self.init_image_twin()
        self.draw_twin = ImageDraw.Draw(self.image_twin)

        self.app = Tk()
        self.app.geometry(str(self.canvas_width) + 'x' + str(self.canvas_height))

        self.canvas = Canvas(self.app, bg='black')
        self.canvas.pack(anchor='nw', fill='both', expand=1)        

        self.canvas.bind('<Button-1>', self.get_xy)
        # Button-3 corresponds to the right mouse button,
        # while Button-2 corresponds to the middle button if available,
        # that might be confusing if not reading the docs of tkinter.
        self.canvas.bind('<Button-3>', self.on_mouse_right_button)
        self.canvas.bind('<B1-Motion>', self.draw_stroke)

        self.app.bind('<space>', self.clear_canvas)
        self.app.bind('<q>', self.quit)
        self.app.bind('<Escape>', self.quit)
        self.app.bind('-', self.decrement_stroke_size)
        # Be careful with your keyboard layout to make sure you actually press
        # '+' key, rather than '=' for example, which both might share the 
        # same physical key on the keyboard.
        self.app.bind('+', self.increment_stroke_size)

        self.app.bind('<Key>', self.key_pressed)
        self.app.bind('<a>', self.append_data)
        self.app.bind('<s>', self.save_data)

        self.app.mainloop()
 
dc = DataCollect(stroke_size=16, canvas_width=200, canvas_height=200)
dc.run()