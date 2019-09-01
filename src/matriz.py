import cv2
import numpy as np
import math

def matrizEscala(x,y):
    matriz = np.array([[x, 0, 0], [0, y, 0], [0, 0, 1]])
    return matriz

def matrizRotacao(ang):
    matriz = np.array([[math.cos(ang), math.sin(ang), 0], [-math.sin(ang), math.cos(ang), 0], [0, 0, 1]])
    return matriz

def matrizTranslacao(x,y):
    matriz = np.array([[1, 0, 0], [0, 1, 0],[x, y, 1]])
    return matriz