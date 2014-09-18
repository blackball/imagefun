#!/usr/bin/python2.7

'''
Get the unique image files from image albumn.
You could backup the unique images by using 
this unique image name list.
'''

import os
from PIL import Image
# used for image hashing: https://github.com/JohannesBuchner/imagehash
# but found: https://github.com/bunchesofdonald/photohash has some more decent routines 
import imagehash 
import shutil

class ImageBackup:
    def __int__(self):
        '''
        '''
        pass
    
    def all_images(self, directory):
        for dirpath,_,filenames in os.walk(directory):
            for f in filenames:
                if f.endswith(".JPG") or f.endswith(".jpg"):
                    yield os.path.abspath(os.path.join(dirpath, f))

    def get(self, folder):
        '''
        find unique images, and return their names
        '''
        hashset = set()
        names = []
        hashfunc = imagehash.average_hash
        counter = 0
        
        all_names = [name for name in self.all_images(folder)]
        print "\nStart find unique image files in %s images:" % (len(all_names))
        for name in all_names:
            val = hashfunc(Image.open(name))
            if not (val in hashset): 
                names.append(name)
                hashset.add(val)
            counter += 1
            if counter%50 == 0: print counter
        print "Done!"
        if counter > 0:
            print "Duplicate ratio: %s/%s = %s\n" % (len(names), counter, len(names)/float(counter))
        return names

    def backup(self, names, folder):
        '''
        Move files in names into folder
        '''
        if len(names) == 0:
            print "No image found!"
            return 
        if not os.path.isdir(folder):
            print "Creating dir: ", folder
            os.makedirs(folder)
        print "Start copying:"
        counter = 0;
        for name in names:
            shutil.copy(name, folder)
            counter += 1
            if counter % 50 == 0: print counter
        print "Done!\n"

if __name__ == "__main__":
    bk = ImageBackup()
    names = bk.get("/home/blackball/Pictures/test")
    bk.backup(names, "/home/blackball/Pictures/backup")
