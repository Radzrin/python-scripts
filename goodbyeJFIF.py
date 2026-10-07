from PIL import Image
import os


from os import listdir
from os.path import isfile, join
mypath = "C:\\Users\\user\\Downloads\\random touhou"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
name = ''

i = 0

for x in onlyfiles:

	if "jfif" in x:
		img = Image.open(f'{mypath}/{x}')

		isExist = os.path.exists(f"{mypath}/{name}{i}.jpg")
		while isExist:
			i += 1
		img.save(f'{mypath}/{name}{i}.jpg')
		os.remove(f'{mypath}/{x}')
		i += 1
	

print("no more jfif")
print(i, "jfif images changed")