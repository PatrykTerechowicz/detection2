import cv2
from detection2.Obraz import ImagePoint as pointIm, Image as im
from detection2.Optymalizacyjne import Genetic as genOpt
#pyscript



print("Wczytuje obrazy:")
port = im.Image('portBlurEdge.jpg')
print("Wczytano")

#NOISY
#TLO INDUSTRIALNE
DOMEK = pointIm.ImagePoint(570, 542, 31, 22, port) #znalazło wodę xd
PRAWY1 = pointIm.ImagePoint(1010, 700, 102, 42, port) #znalazło domek
PRAWY2 = pointIm.ImagePoint(1200, 747, 69, 30, port) #znalazło chmurę
LEWY_VERYNOISY = pointIm.ImagePoint(210, 681, 94, 28, port) #znalazł podobny jacht po lewej



best = genOpt.findBest(PRAWY1, port)
print(f'Znalazlem prawy1 w: x:{best.x}, y:{best.y}, width:{best.width}, height:{best.height}')
best = genOpt.findBest(PRAWY2, port)
print(f'Znalazlem prawy2 w: x:{best.x}, y:{best.y}, width:{best.width}, height:{best.height}')
best = genOpt.findBest(LEWY_VERYNOISY, port)
print(f'Znalazlem lewy_verynoisy w: x:{best.x}, y:{best.y}, width:{best.width}, height:{best.height}')
best = genOpt.findBest(DOMEK, port)
print(f'Znalazlem DOMEK w: x:{best.x}, y:{best.y}, width:{best.width}, height:{best.height}')