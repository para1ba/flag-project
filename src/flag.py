import forms as formas
import cv2
import numpy as np


class Flag():
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.image = np.zeros((height, width, 3), np.uint8)
        pts = np.array([[0,0], [width, 0], [width, height], [0, height]], np.int32)
        cv2.fillPoly(self.image, [pts], background_color)
    
    def drawTriangle(self, dots, color_rgb):
        if(len(dots) == 3):
            formas.drawPolygon(self.image, dots, color_rgb)
        else:
            print("- TRIÂNGULO INVÁLIDO -")
    
    def drawRectangle(self, dots, color_rgb):
        if(len(dots) == 4):
            formas.drawPolygon(self, dots, color_rgb)
        else:
            print("- RETÂNGULO INVÁLIDO -")

    def fillPolygon(self, reference_dot, color_rgb):
        cv2.fillPoly(self.image, reference_dot, color_rgb)
    
    def showFlag(self):
        cv2.imshow('Flag', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def escala(self, timesX, timesY):
        height = self.image.shape[0]
        width = self.image.shape[1]

        newImage = np.zeros((timesY*height, timesY*width, 3), np.uint8)
        pts = np.array([[0,0], [timesX*width, 0], [timesX*width, timesY*height], [0, timesY*height]], np.int32)
        cv2.fillPoly(newImage, [pts], (255 ,255 ,255))

        for i in range(width):
            for j in range(height):
                pix = self.image[j, i]
                y = j*int(timesY)
                x = i*int(timesX)
                if(x < newImage.shape[1] and y < newImage.shape[0]):
                    newImage[y, x] = pix
        self.image = newImage

    def transl(self, x, y):
        width = self.image.shape[0]
        height = self.image.shape[1]

        newImage = np.zeros((width, height, 3), np.uint8)
        pts = np.array([[0,0], [width, 0], [width, height], [0, height]], np.int32)
        cv2.fillPoly(newImage, [pts], (0, 0, 0))

        for i in range(width):
            for j in range(height):
                pixel = self.image[i, j]
                if((i+y) < width and (j+x) < height):
                    newImage[i+y, j+x] = pixel
        self.image = newImage