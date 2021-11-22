import cv2
import numpy as np
import math

class Editor:
    top_left = []
    bottom_right = []
    window_name = ''
    trackbar_name = ''
    image_cached = None
    image = None
    color_edit = [0, 255]
    color_edit_name = 'color_edit'
    selection_color = (0, 255, 0)
    selection_thickness = 10
    lower_blue = []
    upper_blue = []
    mask = None

    def edit_color(self):
        if self.color_edit[0] > 0:
            x0 = self.top_left[0]
            y0 = self.top_left[1]
            w = self.bottom_right[0] - self.top_left[0]
            h = self.bottom_right[1] - self.top_left[1]            

            for i in range(w):
                for j in range(h):
                    yj = y0 + j
                    xi = x0 + i             
                    pixel = self.image[yj, xi]
                    b = pixel[0]
                    g = pixel[1]
                    r = pixel[2]

                    # if b > 1 and r < 255 and g < 255:
                    hsv = self.hsv[yj, xi]
                    # print(hsv[0])
                    # print('[' + str(yj) + ', ' + str(xi) + '] - ' + str(hsv))
                    if self.mask[yj, xi] > 0:
                        print(str(b) + ' ' + str(g) + ' ' + str(r))
                        b = 0
                        g_temp = max(g, r)
                        g_temp = math.floor(g / 2) + math.floor(r / 2)                      
                        r = math.floor(g / 2) + math.floor(r / 2)
                        g = g_temp
                        # r = min(math.floor(1.0 * r), 255)
                        # g = min(math.floor(1.0 * g), 255)                    
                    self.image[y0 + j, x0 + i] = (b, g, r)

    def on_trackbar(self, val):
        self.color_edit[0] = val
        self.image = self.image_cached.copy()
        # cv2.rectangle(self.image, self.top_left, self.bottom_right, self.selection_color, self.selection_thickness)
        self.edit_color()
        self.show_image()

    def show_image(self):
        cv2.imshow(self.window_name, self.image)

    def draw_rectangle(self, action, x, y, flags, *userData):
        if action == cv2.EVENT_LBUTTONDOWN:
            self.top_left = (x, y)            
        elif action == cv2.EVENT_LBUTTONUP:            
            self.bottom_right = (x, y)

            x_left = 0
            x_right = 0
            y_bottom = 0
            y_top = 0
            
            x_left = min(self.top_left[0], self.bottom_right[0])
            x_right = max(self.top_left[0], self.bottom_right[0])
            y_bottom = max(self.top_left[1], self.bottom_right[1])
            y_top = min(self.top_left[1], self.bottom_right[1])
            self.top_left = (x_left, y_top)
            self.bottom_right = (x_right, y_bottom)
            
            self.image = self.image_cached.copy()
            cv2.rectangle(self.image, self.top_left, self.bottom_right, self.selection_color, self.selection_thickness)
            
            self.show_image()

    def main(self):
        imgReadFlag = 1
        self.image = cv2.imread('assets/2.jpg', imgReadFlag)
        self.image = cv2.resize(self.image, (0, 0), fx=0.8, fy=0.8)
        self.image_cached = self.image.copy()

        self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        self.lower_blue = np.array([50,50,50])
        self.upper_blue = np.array([120,255,255])

         # Threshold the HSV image to get only blue colors
        self.mask = cv2.inRange(self.hsv, self.lower_blue, self.upper_blue)
        # Bitwise-AND mask and original image
        self.image = cv2.bitwise_and(self.image, self.image, mask=self.mask)


        self.window_name = 'image'
        self.show_image()
        cv2.setMouseCallback(self.window_name, self.draw_rectangle)
        
        cv2.createTrackbar(self.color_edit_name, self.window_name, self.color_edit[0], self.color_edit[1], self.on_trackbar)

        self.top_left = (50, 50)
        self.bottom_right = (150, 150)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    editor = Editor()
    editor.main()