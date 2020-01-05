#!/usr/bin/env python3.7
import cv2 as cv
import argparse
import os.path

import circles
import binary_eye
import unwrap

min_size_divider = 5

# print("helllo darknes my old friend.....")


parser = argparse.ArgumentParser(description='Preprepare the eye biometry')
parser.add_argument(
    '--binary', '-b', help="Only generate binary files into output folder", action="store_true")
parser.add_argument('--file', '-f', help="Choose file to do the thing with")
parser.add_argument(
    '--output', '-o', help="Choose file name for output", default="./output/out.png")
parser.add_argument('--iris', '-i', help="binary file of iris",
                    default="./gimp_out/small.png")
parser.add_argument('--eye', '-e', help="binary file of eye",
                    default="./gimp_out/big.png")


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

if not os.path.isfile(args.iris) or not os.path.isfile(args.eye):
    raise(FileNotFoundError)

try:
    binary_eye.read_files()
except Exception as e:
    print(e)


male, duze = binary_eye.read_files(name_small=args.iris, name_big=args.eye)

#Operacje wygladzajace
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 2))
duze = cv.dilate(duze, kernel, iterations=2)
male = cv.dilate(male, kernel, iterations=1)

duze = cv.erode(duze, kernel, iterations=5)
male = cv.erode(male, kernel, iterations=4)

male = cv.dilate(male, kernel, iterations=2)


male = circles.fill_holes(male)
duze = circles.fill_holes(duze)

Centrum = {}
Centrum['male'] = circles.find_circles(male)
Centrum['duze'] = circles.find_circles(
    duze, min_size=int(duze.shape[0]/min_size_divider))

pic_unwrapped = unwrap.unwrap(pic, Centrum['male'], Centrum['duze'], duze,remove_unnedeed=False)
pic_unwrapped_removed_unnneded = unwrap.unwrap(pic, Centrum['male'], Centrum['duze'], duze)

circles.show_circles(pic, Centrum['male'])
circles.show_circles(pic, Centrum['duze'])

circles.show_circles(male, circles.find_circles(male))
circles.show_circles(duze, circles.find_circles(
    duze, min_size=int(duze.shape[0]/min_size_divider)))


cv.imshow("lol", pic)
cv.imshow("lol2", male)
cv.imshow("lol3", duze)
cv.imshow("final_unwraped", pic_unwrapped)
cv.waitKey()

cv.imwrite(args.output, pic)
cv.imwrite("./output/unwraped.png", pic_unwrapped)
cv.imwrite("./output/male.png", male)
cv.imwrite("./output/duze.png", duze)
cv.imwrite("./output/unnneded.png", pic_unwrapped_removed_unnneded)



