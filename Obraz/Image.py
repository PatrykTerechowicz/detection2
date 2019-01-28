import cv2
import numpy as np
from detection2.Obraz import image_operations as imOp


class Image:
    def __init__(self, path):
        self.img = prepareImg(cv2.imread(path))
        self.Q = genQMatrix(self.img)
        self.P = genPVector(self.img)
        pass

    #first second are 2 elements tuples
    def cr(self, first, second):
        n = size(first, second)
        QSum = self.Q[second[0], second[1]] + self.Q[first[0], first[1]] - self.Q[first[0], second[1]] - self.Q[second[0], first[1]]
        PSum = self.P[second[0], second[1]] + self.P[first[0], first[1]] - self.P[first[0], second[1]] - self.P[second[0], first[1]]
        PSum = PSum.reshape(9 , 1)@PSum.reshape(1  , 9)
        if(n == 0 ):
            print(f'FIRST: {first[0]}, {first[1]}; SECOND: {second[0]}, {second[1]}')
        return (QSum - PSum/n)/(n)


    def getX(self):
        return self.img.shape[1]-1


    def getY(self):
        return self.img.shape[0]-1


def size(first, second):
    return abs((second[0]-first[0])+1)*(abs(second[1]-first[1])+1)


def genQMatrix(img):
    Q = np.zeros((img.shape[0], img.shape[1], 9, 9))
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            Q[y, x] = img[y,x].reshape(9,1)@img[y, x].reshape(1,9)
    Q = np.cumsum(Q, axis = 0)
    Q = np.cumsum(Q, axis = 1)
    return Q


def genPVector(img):
    S = img
    S = np.cumsum(S, axis=0)
    S = np.cumsum(S, axis=1)
    return S


def prepareImg(img):
    imgShape2 = (img.shape[0], img.shape[1])
    X = np.fromfunction(lambda i, j: j, shape=imgShape2)
    Y = np.fromfunction(lambda i, j: i, shape=imgShape2)
    gray = imOp.grayscale(img)
    eX = imOp.edgeX(gray)
    eXX = imOp.edgeX(eX)
    eY = imOp.edgeY(gray)
    eYY = imOp.edgeY(eY)
    merged = np.zeros((imgShape2[0], imgShape2[1], 9))
    for y in range(imgShape2[0]):
        for x in range(imgShape2[1]):
            merged[y, x] = [X[y,x], Y[y,x], img[y,x,0], img[y,x,1], img[y,x,2], eX[y,x], eXX[y,x], eY[y,x], eYY[y,x]]
    return merged

