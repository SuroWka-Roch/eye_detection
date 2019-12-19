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

    t, small = cv.threshold(pic_gray, p/4.5, 255, cv.THRESH_BINARY,)
    t, big = cv.threshold(pic_gray, p/1.5, 255, cv.THRESH_BINARY,)

    return small, big


def save_files(small, big, name_small="small.png", name_big="big.png"):
    cv.imwrite("./output/{}".format(name_small), small)
    cv.imwrite("./output/{}".format(name_big), big)


def read_files(name_small="small.png", name_big="big.png"):
    small = cv.imread("./output/{}".format(name_small))
    big = cv.imread("./output/{}".format(name_big))

    big = cv.cvtColor(big, cv.COLOR_BGR2GRAY)
    small = cv.cvtColor(small, cv.COLOR_BGR2GRAY)

    print(big.shape)
    return small, big
