import cv2 as cv
import numpy as np
import math

RADIUS = 2
X = 0
Y = 1

NOT_INCLUDED_COLOUR = [255,0,0]

# def remove_empty(pic):
#     to_remove_col =[]
#     for a in range(pic.shape[0]):


#     pic = np.delete(arr2D, to_remove_col, axis=1)

#    return pic
def abs(intiger):
    return intiger if intiger>0 else -intiger


def hight_of_wrap(centrum1, centrum2):
    """Takes circle detect list and returns hight of wrap """

    if centrum1[RADIUS] > centrum2[RADIUS]:
        centrum1, centrum2 = centrum2, centrum1

    #try not to include iris in the unwrapped picture
    hight_of_wrap_value = centrum2[RADIUS]-(centrum1[RADIUS] + \
        math.hypot(centrum1[X]-centrum2[X], centrum1[Y]-centrum2[Y]))

    return abs(int(hight_of_wrap_value))


def unwrap(pic, centrum1, centrum2,picture_to_include,remove_unnedeed = True):
    """Centrum 2 is the circle of the whole eye"""
    if centrum1[RADIUS] > centrum2[RADIUS]:
        centrum1, centrum2 = centrum2, centrum1

    hight = hight_of_wrap(centrum1, centrum2)
    width = hight * 2
    min_hight = int(centrum2[RADIUS] - hight)
    final_pic = np.zeros((hight, width, 3), np.uint8)
    r_range = np.linspace(min_hight, centrum2[RADIUS], num=hight)
    theta_range = np.linspace(0, 2*math.pi, num=width)

    r_counter = 0
    theta_counter = 0
    for r in r_range:
        for theta in theta_range:
            newX = int((r * math.cos(theta)) + centrum2[X])
            newY = int((r * math.sin(theta)) + centrum2[Y])
            pixel_val = pic[newY][newX]
            #sprawdz czy znajduje się w oku.
            if remove_unnedeed:
                if picture_to_include[newY][newX] == 255:
                    pixel_val = NOT_INCLUDED_COLOUR
            final_pic[r_counter][theta_counter] = pixel_val
            theta_counter+=1
        r_counter+=1
        theta_counter = 0

    return final_pic
