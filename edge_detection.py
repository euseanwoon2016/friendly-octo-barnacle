import cv2 as cv
import numpy as np
from utils import rescaleFrame

img = cv.imread('photos/mahjong.png')
rescaled = rescaleFrame(img)
cv.imshow('Mahjong', rescaled)


cv.waitKey(0)