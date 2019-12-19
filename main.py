#!/usr/bin/env python3.7
import cv2 as cv
import circles


def prog(img):
    """Wyliczenie średniej wartości piksela dla obrazu zbinaryzowanego. Wartość średnia"""
    p = 0
    for w in img:
        for h in w:
            p += h
    return (p/(img.shape[0]*img.shape[1]))



print("helllo darknes my old friend.....")
pic = cv.imread("./fig/01.png")


pic_gray = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)

p = prog(pic_gray)

t, male = cv.threshold(pic_gray, p/4.5, 255, cv.THRESH_BINARY,)
t, duze = cv.threshold(pic_gray, p/1.5, 255, cv.THRESH_BINARY,)



circles.show_circles(pic, circles.find_circles(male))
circles.show_circles(pic, circles.find_circles(duze))


cv.imshow("lol", pic)
cv.imshow("lol2", male)
cv.imshow("lol3", duze)


cv.waitKey()
