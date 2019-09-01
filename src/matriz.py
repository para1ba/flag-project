import cv2
import math
import numpy as np

def matriz_escala(x_scale, y_scale):
    return np.array([[x_scale, 0, 0], 
                     [0, y_scale, 0], 
                     [0, 0, 1]])

def matriz_rotacao(degrees):
    return np.array([[math.cos(degrees), -math.sin(degrees), 0], 
                     [math.sin(degrees), math.cos(degrees), 0], 
                     [0, 0, 1]])

def matriz_translacao(x_factor, y_factor):
    return np.array([[1, 0, x_factor], 
                     [0, 1, y_factor],
                     [0, 0, 1]])

def apply_transformation(x, y, matrix):
    a = np.array([[x], [y], [1]])
    b = np.matmul(matrix, a)
    print(a)
    print("#####")
    print(b)

    #return resp[0], resp[1]
