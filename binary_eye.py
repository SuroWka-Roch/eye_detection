import cv2 as cv

def prog(img):
    """Wyliczenie średniej wartości piksela dla obrazu zbinaryzowanego. Wartość średnia"""
    p = 0
    for w in img:
        for h in w:
            p += h
    return (p/(img.shape[0]*img.shape[1]))



def make_binary(img):
    pic_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    p = prog(pic_gray)

    t, small  = cv.threshold(pic_gray, p/4.5, 255, cv.THRESH_BINARY,)
    t, big = cv.threshold(pic_gray, p/1.5, 255, cv.THRESH_BINARY,)

    return small ,big