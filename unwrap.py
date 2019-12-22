import cv2 as cv
import numpy as np
import math

RADIUS = 2
X = 0
Y = 1


def hight_of_wrap(centrum1, centrum2):
    """Takes circle detect list and returns hight of wrap """

    if centrum1[RADIUS] > centrum2[RADIUS]:
        centrum1, centrum2 = centrum2, centrum1

    #try not to include iris in the unwrapped picture
    hight_of_wrap_value = centrum2[RADIUS]-(centrum1[RADIUS] + \
        math.hypot(centrum1[X]-centrum2[X], centrum1[Y]-centrum2[Y]))

    return int(hight_of_wrap_value)


def unwrap(pic, centrum1, centrum2):
    """Centrum 2 is the circle of the whole eye"""
    if centrum1[RADIUS] > centrum2[RADIUS]:
        centrum1, centrum2 = centrum2, centrum1

    hight = hight_of_wrap(centrum1, centrum2)
    width = hight * 2
    min_hight = int(centrum2[RADIUS] - hight)
    final_pic = np.zeros((hight, width, 3), np.uint8)
    r_range = np.linspace(min_hight, centrum2[RADIUS], num=hight)
    theta_range = np.linspace(0, 2*math.pi, num=width)
    for r in r_range:
        for theta in theta_range:
            newX = int((r * math.cos(theta)) + centrum2[X])
            newY = int((r * math.sin(theta)) + centrum2[Y])
            pixel_val = pic[newY][newX]
            final_pic[int(r)-min_hight-1][int(theta *
                                              width/(2*math.pi))-1] = pixel_val

    return final_pic
