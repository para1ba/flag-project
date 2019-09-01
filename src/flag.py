import forms as formas
import cv2
import numpy as np
import math

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
        width = self.image.shape[0]
        height = self.image.shape[1]

        newImage = np.zeros((timesY*height, timesX*width, 3), np.uint8)
        pts = np.array([[0,0], [timesY*width, 0], [timesY*width, timesX*height], [0, timesX*height]], np.int32)
        cv2.fillPoly(newImage, [pts], (255 ,255 ,255))

        for i in range(self.image.shape[0]):
            for j in range(self.image.shape[1]):
                pix = self.image[i][j]
                x = i*timesY
                y = j*timesX
                newImage[x][y] = self.image[i][j]
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

    def blank_copy(self):
        resp = np.zeros((self.height, self.width, 3), np.uint8)
        pts = np.array([[0,0], [self.width, 0], [self.width, self.height], [0, self.height]], np.int32)
        cv2.fillPoly(resp, [pts], (255, 255, 255))

        return resp

    def rotate(self, degrees):
        aux_image = self.blank_copy()
        for i in range(self.width):
            for j in range(self.height):
                pixel = self.image[j, i]
                new_x = abs(math.trunc(math.cos(degrees) * i) + math.trunc(math.sin(degrees) * j))
                new_y = abs(math.trunc(-math.sin(degrees) * i) + math.trunc(math.cos(degrees) * j))
                #print(new_x, new_y)
                if(new_x < self.width and new_x > 0 and new_y < self.height and new_y > 0):
                    aux_image[new_y, new_x] = pixel
        self.image = aux_image