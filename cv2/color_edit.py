import cv2

class Editor:
    top_left = []
    bottom_right = []
    window_name = ''
    trackbar_name = ''
    image_cached = None
    image = None
    color_edit = [0, 255]
    color_edit_name = 'color_edit'

    def edit_color(self):
        if self.color_edit[0] > 0:
            x0 = self.top_left[0]
            y0 = self.top_left[1]
            w = self.bottom_right[0] - self.top_left[0]
            h = self.bottom_right[1] - self.top_left[1]

            print('top_left == ' + str(self.top_left))
            print('top_right == ' + str(self.bottom_right))
            print('x0 == ' + str(x0))
            print('y0 == ' + str(y0))

            print('w == ' + str(w))
            print('h == ' + str(h))

            for i in range(w):
                for j in range(h):                    
                    self.image[y0 + j, x0 + i] = (0, 255, 0)

    def on_trackbar(self, val):
        self.color_edit[0] = val
        self.edit_color()
        self.show_image()

    def show_image(self):
        cv2.imshow(self.window_name, self.image)

    def draw_rectangle(self, action, x, y, flags, *userData):
        if action == cv2.EVENT_LBUTTONDOWN:
            self.top_left = (x, y)
            print(x, y)
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

            color = (0, 255, 0)
            thickness = 10
            self.image = self.image_cached.copy()
            cv2.rectangle(self.image, self.top_left, self.bottom_right, color, thickness)
            
            self.show_image()

    def main(self):
        imgReadFlag = 1
        self.image = cv2.imread('assets/lenna.png', imgReadFlag)
        self.image = cv2.resize(self.image, (0, 0), fx=1.5, fy=1.5)
        self.image_cached = self.image.copy()

        self.window_name = 'image'
        self.show_image()
        cv2.setMouseCallback(self.window_name, self.draw_rectangle)

        print(type(self.image))
        print(self.image.shape)
        print(self.image[0])
        
        cv2.createTrackbar(self.color_edit_name, self.window_name, self.color_edit[0], self.color_edit[1], self.on_trackbar)

        self.top_left = (50, 50)
        self.bottom_right = (150, 150)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    editor = Editor()
    editor.main()