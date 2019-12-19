import cv2 as cv

def show_circles(img, location):
    """show pictures in colour with the location of iris
    location list of circles to print to picture
    img: rbg picture of eye
    """
    cv.circle(img, (location[0], location[1]), location[2], (255, 0, 255), 1)
    cv.circle(img, (location[0], location[1]), 1, (255, 0, 255), 1)




def find_circles(img, param2=130):
    while True:
        temp = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 10, minRadius=int(
            img.shape[1]/9), param1=1, param2=param2)
        if temp is not None:
            break
        param2 += -1
    return temp[0][0]
