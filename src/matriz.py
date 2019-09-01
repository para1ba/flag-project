import cv2
import math

def matrizEscala(x,y):
    matriz = [[x, 0, 0], [0, y, 0], [0, 0, 1]]
    return matriz

def matrizRotacao(ang):
    matriz = [[math.cos(ang), math.sin(ang), 0], [-math.sin(ang), math.cos(ang), 0], [0, 0, 1]]
    return matriz

def matrizTranslacao(x,y):
    matriz = [[1, 0, 0], [0, 1, 0],[x, y, 1]]
    return matriz