#!/usr/bin/env python3.7
import cv2 as cv


def prog(img):
    """Wyliczenie średniej wartości piksela dla obrazu zbinaryzowanego. Wartość średnia"""
    p = 0
    for w in img:
        for h in w:
            p += h
    return (p/(img.shape[0]*img.shape[1]))


def show_circles(img, location):
    """show pictures in colour with the location of iris
    location list of circles to print to picture
    img: rbg picture of eye
    """
    for point in location:
        cv.circle(img, (point[0], point[1]), point[2], (255, 0, 255), 1)
        cv.circle(img, (point[0], point[1]), 1, (0, 255, 0), 1)


print("helllo darknes my old friend.....")
pic = cv.imread("./fig/01.png")


pic_gray = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)

p = prog(pic_gray)

t, male = cv.threshold(pic_gray, p/4.5, 255, cv.THRESH_BINARY,)
t, duze = cv.threshold(pic_gray, p/1.5, 255, cv.THRESH_BINARY,)

circle_list = []

param2 = 130
while True:
    lista = cv.HoughCircles(duze, cv.HOUGH_GRADIENT, 1, 10, minRadius=int(
        pic.shape[1]/9), param1=1, param2=param2)
    if lista is not None:
        break
    param2 += -1
circle_list.append(lista[0][0])

param2 = 130
while True:
    lista = cv.HoughCircles(male, cv.HOUGH_GRADIENT, 1, 10, minRadius=int(
        pic.shape[1]/24), param1=1, param2=param2)
    if lista is not None:
        break
    param2 += -1
circle_list.append(lista[0][0])
show_circles(pic, circle_list)

cv.imshow("lol", pic)
cv.imshow("lol2", male)
cv.imshow("lol3", duze)


cv.waitKey()
