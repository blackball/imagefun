#!/usr/bin/python2.7

'''
Get all images and randomly select some of them to generate a snapshot.
'''
import os
import PIL
import random
from PIL import Image, ImageOps

class Snapshot:
    def __init__(self):
        self.num = 20
        self.icon_size = [20,20]

    def set_num(self, n):
        self.num = n

    def set_icon_size(sz):
        self.icon_size = sz

    def all_images(self, directory):
        for dirpath,_,filenames in os.walk(directory):
            for f in filenames:
                if f.endswith(".JPG"):
                    yield os.path.abspath(os.path.join(dirpath, f))
    
    def next_box(self):
        w = self.icon_size[0]
        h = self.icon_size[1]
        for i in xrange(self.num):
            for j in xrange(self.num):
                x = j*w
                y = i*h
                yield [x, y, x+w, y+h]

    def generate(self, name, dst):
        names = [name for name in self.all_images(name)]
        ids = random.sample(xrange(len(names)), self.num**2)
        big = Image.new("RGB", [s * self.num for s in self.icon_size])
        counter = 0
        _open = Image.open
        _fit = ImageOps.fit
        _paste = big.paste
        method = Image.ANTIALIAS
        for id, box in zip(ids, self.next_box()):
            im = _open( names[id])
            icon = _fit(im, self.icon_size, method)
            _paste(icon, box)
            print counter
            counter += 1
        big.save(dst, "JPEG")

if __name__ == "__main__":
    sp = Snapshot()
    sp.generate("/home/blackball/Pictures/", "snapshot.jpg")
