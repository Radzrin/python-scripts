from PIL import Image, ImageSequence
import os
from os import listdir
from os.path import isfile, join
mypath = "E:\\usb fr fr\\idk\\OG\\uma"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
loop = 0
name = "twinturbo"

def IsAGif(FilePath, loop):
    try:
        MediaFile = Image.open(FilePath)
        Index = 0
        for Frame in ImageSequence.Iterator(MediaFile):
            Index += 1
        if Index > 1: #Must mean the the .webp is a gif because it has more than one frame
            im = Image.open(f"{FilePath}").convert("RGB")
            im.save(f"{mypath}/{name}gif{loop}.gif", "gif")
            im.close()
            return True
        else: #Must mean that the .webp has 1 frame which makes it a image
            im = Image.open(f"{FilePath}").convert("RGB")
            im.save(f"{mypath}/{name}{loop}.png", "png")
            im.close()
        MediaFile.close()    
        return False
    except: #If the .webp can't be opened then it is most likely not a .gif or .webp
        im.close()
        return False


for w in onlyfiles:
    if f"{name}{loop}" in w or f"{name}gif{loop}" in w:
        loop += 1

    isExist = os.path.exists(f"{mypath}/{name}{loop}.png") 
    isExistgif = os.path.exists(f"{mypath}/{name}gif{loop}.gif") 
    if(isExist or isExistgif):    
        loop += 1

for x in onlyfiles:
    if "webp" in x:
        IsAGif(f"{mypath}/{x}", loop)
        loop += 1

for y in onlyfiles:
    if "webp" in y:
        os.remove(f"{mypath}/{y}")


