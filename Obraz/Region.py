from detection2.Obraz import Image as im
import math

class Region:
    #defined region from image
    def __init__(self, first, second, img:im.Image):
        self.first = first
        self.second = second
        self.img = img
        self.cr = img.cr(first, second)


    def getCRS(self):
        CR1 = self.cr
        first = self.first
        second = self.second
        CR2 = self.img.cr(first, (math.ceil((second[0]+first[0])/2), second[1]))
        CR3 = self.img.cr(first, (second[0], math.ceil((second[1]+first[1])/2)))
        CR4 = self.img.cr((first[0], math.floor((first[1]+second[1])/2)), second)
        CR5 = self.img.cr((math.floor((first[0]+second[0])/2), first[1]), second)
        return (CR1, CR2, CR3, CR4, CR5)