from PIL import Image
import os


from os import listdir
from os.path import isfile, join
mypath = ""
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

i = 0

for x in onlyfiles:

	img = Image.open(f'{mypath}/{x}')

	img.save(f'{mypath}/ark{i}.png')
	if i != 10:
		os.remove(f'{mypath}/{x}')
	i += 1
	

print("changed the names")