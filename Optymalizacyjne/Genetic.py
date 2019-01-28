from detection2.Obraz import ImagePoint as pointIm, Image as im
import scipy.linalg as eigh
import math
from random import random
from random import randint
from random import shuffle
maxgen = 100
epsilon = 0.01
mutationchance = 1/2
def findBest(src:pointIm.ImagePoint, img:im.Image) -> pointIm.ImagePoint:
    pop = []
    maxpop = 0
    for i in range(0, img.getX(), 23):
        for j in range(0, img.getY(), 23):
            maxpop = maxpop + 1
            pop.append(pointIm.ImagePoint(i, j, 23, 23, img))
    minpop = 32
    srcCR = src.getCR()

    maxpop = pop.__len__()



    gen = 0
    while(gen<maxgen):
        if(gen%(maxgen/5) == 0):
            print(f'generacja: {gen}')
        #selekcja
        pop = tournament(srcCR, pop)
        #mutacja
        for p in pop:
            if(random() < mutationchance):
                mutate(p)
        #usuwanie czesci populacji
        if(maxpop > minpop):
            maxpop = math.floor(maxpop*0.8)
            if(maxpop < minpop):
                maxpop = 32
        #krzyżowanie
        ln = len(pop)
        for i in range(ln, maxpop):
            n1 = randint(0, math.floor(len(pop)/2))
            n2 = randint(math.floor(len(pop)/2), len(pop)-1)
            pop.append(crossover(pop[n1], pop[n2]))
        gen += 1
    return minDistPoint(srcCR, pop)


def mutate(p:pointIm.ImagePoint):
    x1 = randint(-2, 2)
    y1 = randint(-2, 2)
    p.move(y1, x1)
    x1 = randint(-4, 4)
    y1 = randint(-4, 4)
    p.resize(y1, x1)


def crossover(p1:pointIm.ImagePoint, p2:pointIm.ImagePoint):
    x, y = 0, 0
    height, width = 0, 0
    if(randint(0, 1) == 0):
        x = p1.x
    else:
        x = p2.x
    if(randint(0, 1) == 0):
        y = p1.y
    else:
        y = p2.y
    if(randint(0, 1) == 0):
        height = p1.height
    else:
        height = p2.height
    if(randint(0, 1) == 0):
        width = p1.width
    else:
        width = p2.width
    return pointIm.ImagePoint(x, y, width, height, p1.img)


#only used in calculating dist
def crDist(cr0, cr1):
    eigv = eigh.eigvals(cr0, cr1)
    sum = 0
    for val in eigv:
        sum += pow(math.log(abs(val), math.e), 2)
    return math.sqrt(sum)


#used for sorting population array
def dist(srcCR, point:pointIm.ImagePoint):
    sums = []
    cr0 = srcCR
    cr1 = point.getCR()
    for i in range(5):
        sums.append(crDist(cr0[i], cr1[i]))
    sums.sort()
    return sums[0]


def  minDistPoint(srcCR, pop) -> pointIm.ImagePoint:
    min = dist(srcCR, pop[0])
    ndx = 0
    for i in range(1, len(pop)):
        dst = dist(srcCR, pop[i])
        if(dst < min):
            min = dst
            ndx = i
    return pop[i]


#best of 2? tournament
def tournament(srcCR, pop):
    i = 0
    newPop = []
    if(len(pop)%2 != 0):
        i = 1
    for k in range(i, len(pop), 2):
        if(dist(srcCR, pop[k]) < dist(srcCR, pop[k+1])):
            newPop.append(pop[k])
        else:
            newPop.append(pop[k+1])
    return newPop
