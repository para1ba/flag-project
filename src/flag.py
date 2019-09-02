import forms as formas
import cv2
import numpy as np
import math
import matriz as matriz

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

    def fillPolygon(self, reference_dot, color_rgb):
        mask = np.zeros((self.height+2, self.width+2), np.uint8)
        mask[:] = 0
        flags = 4
        cv2.floodFill(self.image, mask, reference_dot, color_rgb, flags)
    
    def showFlag(self):
        cv2.imshow('Flag', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def scale(self, timesX, timesY):
        newImage = self.large_image(timesX, timesY)
        tr = matriz.matriz_escala(timesX, timesY)
        for i in range(self.width):
            for j in range(self.height):
                vlr = matriz.apply_transformation(i, j, tr)
                newImage[vlr[1], vlr[0]] = self.image[j, i]
        self.image = newImage
        self.width = self.image.shape[1]
        self.height = self.image.shape[0]

    def translation(self, x, y):
        newImage = self.black_copy()
        tr = matriz.matriz_translacao(x, y)
        for i in range(self.width):
            for j in range(self.height):
                vlr = matriz.apply_transformation(i, j, tr)
                if(vlr[1] < self.height and vlr[0] < self.width):
                    newImage[vlr[1], vlr[0]] = self.image[j, i]
        self.image = newImage

    def large_image(self, timesX, timesY):
        resp = np.zeros((self.height*timesY, self.width*timesX, 3), np.uint8)
        pts = np.array([[0,0], [self.width*timesX, 0], [self.width*timesX, self.height*timesY], [0, self.height*timesY]], np.int32)
        cv2.fillPoly(resp, [pts], (0, 0, 0))

        return resp

    def black_copy(self):
        resp = np.zeros((self.height, self.width, 3), np.uint8)
        pts = np.array([[0,0], [self.width, 0], [self.width, self.height], [0, self.height]], np.int32)
        cv2.fillPoly(resp, [pts], (0, 0, 0))

        return resp

    def blank_copy(self):
        resp = np.zeros((self.height, self.width, 3), np.uint8)
        pts = np.array([[0,0], [self.width, 0], [self.width, self.height], [0, self.height]], np.int32)
        cv2.fillPoly(resp, [pts], (255, 255, 255))

        return resp

    def rotate(self, degrees):
        newImage = self.black_copy()
        tr = matriz.matriz_rotacao(degrees)
        for i in range(self.width):
            for j in range(self.height):
                vlr = matriz.apply_transformation(i, j, tr)
                if(vlr[1] < self.height and vlr[0] < self.width and vlr[1] > 0 and vlr[0] > 0):
                    newImage[int(vlr[1]), int(vlr[0])] = self.image[j, i]
        self.image = newImage

