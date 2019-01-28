from detection2.Obraz import Image as im
from random import randint
import math
#Wykorzystywany w optymalizacyjnych algorytmach
class ImagePoint:
    def __init__(self, x, y, width, height, img:im.Image):
        self.x = x
        self.y = y
        self.img = img
        self.width = width
        self.height = height
        self.maxX = math.floor(self.img.getX() / 2)
        self.maxY = math.floor(self.img.getY() / 2)


    def getFirst(self):
        yB = self.img.getY()
        xB = self.img.getX()
        y = max(0, min(yB, math.floor(self.y-(self.height/2))))
        x = max(0, min(xB, math.floor(self.x-(self.width/2))))
        return (y, x)


    def getSecond(self):
        yB = self.img.getY()
        xB = self.img.getX()
        y = max(0, min(yB, math.ceil(self.y + (self.height/2))))
        x = max(0, min(xB, math.ceil(self.x + (self.width/2))))
        return (y, x)


    def move(self, y1, x1):
        yB = self.img.getY()
        xB = self.img.getX()
        self.x = max(11, min(xB-11, self.x+x1))
        self.y = max(11, min(yB-11, self.y+y1))

    #max image size is img.X/2 x img.Y/2, min 10x10
    def resize(self, y1, x1):
        maxX = self.maxX
        maxY = self.maxY
        self.height = abs(self.height)
        self.width = abs(self.width)
        self.height = max(10, min(maxY, self.height+y1))
        self.width = max(10, min(maxX, self.width+x1))


    def getCR(self):
        first = self.getFirst()
        second = self.getSecond()
        CR1 = self.img.cr(first, second)
        CR2 = self.img.cr(first, (math.ceil((second[0]+first[0])/2), second[1]))
        CR3 = self.img.cr(first, (second[0], math.ceil((second[1]+first[1])/2)))
        CR4 = self.img.cr((first[0], math.floor((first[1]+second[1])/2)), second)
        CR5 = self.img.cr((math.floor((first[0]+second[0])/2), first[1]), second)
        return (CR1, CR2, CR3, CR4, CR5)


#initializes 11x11 region at random point on image
def randomPoint(img:im.Image):
    x = randint(11, img.getX()-11)
    y = randint(11, img.getY()-11)
    width = 11
    height = 11
    point = ImagePoint(x, y, width, height, img)
    return point