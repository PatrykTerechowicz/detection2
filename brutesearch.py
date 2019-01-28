from detection2.Obraz import Region as rg
from detection2.Obraz import Image as im
import math
import scipy.linalg as eigh

def distWhole(rg1:rg.Region, rg2:rg.Region):
    sum = 0
    vals = eigh.eigvals(rg1.cr, rg2.cr)
    for val in vals:
        sum += math.pow(math.log(abs(val) , math.e) , 2)
    return math.sqrt(sum)


def distCR(cr1, cr2):
    sum = 0
    vals = eigh.eigvals(cr1, cr2)
    for val in vals:
        sum += math.pow(math.log(abs(val), math.e), 2)
    return math.sqrt(sum)



def dissimilarity(rg1:rg.Region, rg2:rg.Region):
    jots = []
    for j in range(0, 4):
        sumk = 0

        for i in range(0, 4):
            sumk += distCR()
    pass

def findBest(searchRegion:rg.Region, img:im.Image):
    options = []
    maxX = img.getX()
    maxY = img.getY()
    baseWidth = searchRegion.second[1] - searchRegion.first[1]
    baseHeight = searchRegion.second[0] - searchRegion.first[0]
    for scale in range(1, 9):
        for y in range(0, maxY, 2+scale):
            for x in range(0, maxX, 2+scale):
                first = (y, x)
                thisWidth = math.ceil((0.55 * 0.15 * (scale - 1)) * baseWidth)
                thisHeight = math.ceil((0.55 * 0.15 * (scale - 1)) * baseHeight)
                second = (y+thisHeight, x+thisWidth)
                options.append(rg.Region(first, second, img))
    #searching for 1000 best matching based of covariance of whole region
    thousandBest = []
    for k in range(0, 999):
        min = options[0]
        minVal = distWhole(options[0], searchRegion)
        for i in range(0, len(options)):
            dst = distWhole(options[i], searchRegion)
            if(minVal > dst):
                minVal = dst
                min = options[i]
        thousandBest.append(min)
        options.remove(min)
