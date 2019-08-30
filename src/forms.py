import cv2
import math

def drawPolygon(image, dots, color_rgb):
    for i in range(len(dots) - 1):
        drawLine(image, dots[i], dots[i + 1], color_rgb)
    drawLine(image, dots[0], dots[len(dots)-1], color_rgb)

def drawLine(image, dot_1, dot_2, color_rgb):
    '''
        Um ponto a se levar em consideração é que não tô pintando os vértices iniciais,
        se o preenchimento vazar talvez esse seja o motivo
    '''
    mid_dot = ((dot_1[0] + dot_2[0])//2, (dot_1[1] + dot_2[1])//2)
    image[mid_dot[1], mid_dot[0]] = color_rgb
    if twoDotsDistance(dot_1, dot_2) > 2:
        drawLine(image, dot_1, mid_dot, color_rgb)
        drawLine(image, mid_dot, dot_2, color_rgb)
    
def twoDotsDistance(dot_1, dot_2):
    return abs(math.sqrt(math.pow(dot_2[0] - dot_1[0], 2) + math.pow(dot_2[1] - dot_1[1], 2)))