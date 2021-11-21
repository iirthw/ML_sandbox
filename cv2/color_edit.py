import cv2

class Editor:
    top_left_corner = []
    bottom_right_corner = []
    window_name = ''
    trackbar_name = ''
    image_cached = None
    image = None
    color_edit = (0, 255)
    color_edit_name = 'color_edit'

    def on_click(self, *args):
        pass

    def draw_rectangle(self, action, x, y, flags, *userData):
        if action == cv2.EVENT_LBUTTONDOWN:
            self.top_left_corner = (x, y)
        elif action == cv2.EVENT_LBUTTONUP:
            self.bottom_right_corner = (x, y)
            color = (0, 255, 0)
            thickness = 10
            self.image = self.image_cached.copy()
            cv2.rectangle(self.image, self.top_left_corner, self.bottom_right_corner, color, thickness)
            cv2.imshow(self.window_name, self.image)

    def main(self):
        imgReadFlag = 1
        self.image = cv2.imread('assets/lenna.png', imgReadFlag)
        self.image = cv2.resize(self.image, (0, 0), fx=1.5, fy=1.5)
        self.image_cached = self.image.copy()

        self.window_name = 'image'
        cv2.imshow(self.window_name, self.image)
        cv2.setMouseCallback(self.window_name, self.draw_rectangle)

        print(type(self.image))
        print(self.image.shape)
        print(self.image[0])
        
        cv2.createTrackbar(self.color_edit_name, self.window_name, self.color_edit[0], self.color_edit[1], self.on_click)        

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    editor = Editor()
    editor.main()