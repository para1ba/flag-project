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
        pass
    
    def showFlag(self):
        cv2.imshow('Flag', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()