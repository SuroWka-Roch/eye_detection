import cv2 as cv
import numpy as np


def show_circles(img, location):
    """show pictures in colour with the location of iris
    location list of circles to print to picture
    img: rbg picture of eye
    """
    cv.circle(img, (location[0], location[1]), location[2], (135, 0, 40), 1)
    cv.circle(img, (location[0], location[1]), 1, (60, 190, 160), 1)


def find_circles(img, param2=130, min_size=0):
    while True:
        temp = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1,
                               10, minRadius=min_size, param1=300, param2=param2)
        if temp is not None:
            break
        param2 += -1
    return temp[0][0]


def fill_holes(img):
    """Fill holes in binary image"""
    hight = img.shape[0]
    width = img.shape[1]

    im_flood = ~img.copy()

    mask = np.zeros((hight+2, width+2), np.uint8)
    cv.floodFill(im_flood, mask, (0, 0), 255)

    pic_final = im_flood & img

    return pic_final
