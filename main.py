#!/usr/bin/env python3.7
import cv2 as cv
import argparse
import os.path

import circles
import binary_eye


print("helllo darknes my old friend.....")


parser = argparse.ArgumentParser(description='Preprepare the eye biometry')
parser.add_argument(
    '--binary', '-b', help="Only generate binary files into output folder", action="store_true")
parser.add_argument('--file', '-f', help="Choose file to do the thing with")
parser.add_argument('--output', '-o', help="Choose file name for output", default="out.png")


args = parser.parse_args()

if args.file:
    FILE_NAME = args.file
else:
    FILE_NAME = "./fig/01.png"

#handle oppening the file
pic = cv.imread(FILE_NAME)
if not os.path.isfile(FILE_NAME):
    if not os.path.isfile("./fig/{}".format(FILE_NAME)):
        raise(FileNotFoundError)
    else:
        pic = cv.imread("./fig/{}".format(FILE_NAME))


if args.binary:
    print("Generating Binary files")
    male, duze = binary_eye.make_binary(pic)
    binary_eye.save_files(male, duze)
    exit()

try:
    binary_eye.read_files()
except Exception as e:
    print(e)


male, duze = binary_eye.read_files()

circles.show_circles(pic, circles.find_circles(male))
circles.show_circles(pic, circles.find_circles(duze))


cv.imshow("lol", pic)
cv.imshow("lol2", male)
cv.imshow("lol3", duze)


cv.imwrite(args.output,pic)

cv.waitKey()
