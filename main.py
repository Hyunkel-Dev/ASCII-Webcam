from cv2 import cv2
import numpy as np
from config import *


class Webcam:

    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.height = None

    def loop(self):
        cond = self.video.isOpened()
        while cond:
            cond, image = self.video.read()
            print(self.convert(image))
            key = cv2.waitKey(1000 // FPS)
            if key == STOP_KEY:
                break

    def convert(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if self.height is None:
            h, w = image.shape
            self.height = round(h * WIDTH * (8 / 21) / w)

        h, w = image.shape
        dw = w / WIDTH
        dh = h / self.height

        string = ""
        for y in range(self.height):
            line = ""
            for x in range(WIDTH):
                value = np.mean(image[int(y * dh):min(int((y + 1) * dh), h), int(x * dw):min(int((x + 1) * dw), w)])
                index = round(value * len(ASCII) // 256)
                line += ASCII[index]
            string += line + "\n"
        return string


if __name__ == '__main__':
    webcam = Webcam()
    webcam.loop()
