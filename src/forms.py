import cv2
import math

def drawPolygon(dots, color_rgb):
    pass
    '''
    for i in range(len(dots) - 2):
        print(i)
        drawLine(dots[i], dots[i + 1], color_rgb)
    drawLine(dots[len(dots) - 1], dots[0], color_rgb)
    '''

def drawLine(dot_1, dot_2, color_rgb):
    actual_dot = dot_1
    while(actual_dot != dot_2):
        best_dot = actual_dot
        best_distance = math.inf
        if twoDotsDistance((actual_dot[0] + 1, actual_dot[1]), dots_2) < best_distance:
            best_distance = twoDotsDistance((actual_dot[0] + 1, actual_dot[1]), dots_2)
            best_dot = (actual_dot[0] + 1, actual_dot[1])
        if twoDotsDistance((actual_dot[0] + 1, actual_dot[1] + 1), dots_2) < best_distance:
            best_distance = twoDotsDistance((actual_dot[0] + 1, actual_dot[1] + 1), dots_2)
            best_dot = (actual_dot[0] + 1, actual_dot[1] + 1)
        if twoDotsDistance((actual_dot[0], actual_dot[1] + 1), dots_2) < best_distance:
            best_distance = twoDotsDistance((actual_dot[0], actual_dot[1] + 1), dots_2)
            best_dot = (actual_dot[0], actual_dot[1] + 1)
        if twoDotsDistance((actual_dot[0] - 1, actual_dot[1]+1), dots_2) < best_distance:
            best_distance = twoDotsDistance((actual_dot[0] - 1, actual_dot[1]+1), dots_2)
            best_dot = (actual_dot[0] - 1, actual_dot[1]+1)
        if twoDotsDistance((actual_dot[0] - 1, actual_dot[1]), dots_2) < best_distance:
            best_distance = twoDotsDistance((actual_dot[0] - 1, actual_dot[1]), dots_2)
            best_dot = (actual_dot[0] - 1, actual_dot[1])
        if twoDotsDistance((actual_dot[0] - 1, actual_dot[1] - 1), dots_2) < best_distance:
            best_distance = twoDotsDistance((actual_dot[0] - 1, actual_dot[1] - 1), dots_2)
            best_dot = (actual_dot[0] - 1, actual_dot[1] - 1)
        if twoDotsDistance((actual_dot[0], actual_dot[1] - 1), dots_2) < best_distance:
            best_distance = twoDotsDistance((actual_dot[0], actual_dot[1] - 1), dots_2)
            best_dot = (actual_dot[0], actual_dot[1] - 1)
        if twoDotsDistance((actual_dot[0] + 1, actual_dot[1] - 1), dots_2) < best_distance:
            best_distance = twoDotsDistance((actual_dot[0] + 1, actual_dot[1] - 1), dots_2)
            best_dot = (actual_dot[0] + 1, actual_dot[1] - 1)
        ## PUT PIXEL ON THE IMAGE
        actual_dot = best_dot

def twoDotsDistance(dot_1, dot_2):
    return math.sqrt(math.pow(dot_1[0] - dot_1[0], 2) + math.pow(dot_1[0] - dot_1[0], 2))