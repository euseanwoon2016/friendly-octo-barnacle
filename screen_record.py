import cv2 as cv
import numpy as np
from mss import mss
from utils import rescale_frame

mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
with mss() as sct:
    while True:
        img = np.array(sct.grab(mon))
        resized = rescale_frame(img)

        cv.imshow('Image', resized)

        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break
