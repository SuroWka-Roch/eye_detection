#!/usr/bin/env python3.7
import cv2 as cv
import argparse

import circles
import binary_eye



print("helllo darknes my old friend.....")
pic = cv.imread("./fig/01.png")

male,duze = binary_eye.make_binary(pic)

circles.show_circles(pic, circles.find_circles(male))
circles.show_circles(pic, circles.find_circles(duze))


cv.imshow("lol", pic)
cv.imshow("lol2", male)
cv.imshow("lol3", duze)


cv.waitKey()
