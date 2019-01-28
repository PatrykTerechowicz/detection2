import numpy as np
import cv2

edgeX_kernel = np.empty((3,3))
edgeX_kernel[0][0] = 1
edgeX_kernel[1][0] = 2
edgeX_kernel[2][0] = 1
edgeX_kernel[0][2] = -1
edgeX_kernel[1][2] = -2
edgeX_kernel[2][2] = -1

edgeY_kernel = np.empty((3,3))
edgeY_kernel[0][0] = 1
edgeY_kernel[0][1] = 2
edgeY_kernel[0][2] = 1
edgeY_kernel[2][0] = -1
edgeY_kernel[2][1] = -2
edgeY_kernel[2][2] = -1

def imshow(win, img):
    cv2.imshow(win, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def edgeX(img):
    return cv2.filter2D(img, -1, edgeX_kernel)


def edgeY(img):
    return cv2.filter2D(img, -1, edgeY_kernel)