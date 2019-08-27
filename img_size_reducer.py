# Image size resizer

# Importing importnat library

import os
from PIL import Image

img_dir_name = "images"
img_height = 900
img_width = 1500
log_file = open("log.txt", "w")
log_count = 0
img_count = 0

for root, dirs, files in os.walk(img_dir_name):
	for file in files:
		img_count += 1
		image = os.path.join(root, file)
		img_attr = Image.open(image)
		# print("Current size : ",str(img_attr.size))
		img_attr = img_attr.resize((img_width,img_width), Image.ANTIALIAS)
		img_attr.save(image, optimize=True, quality=75)
		# print(os.path.getsize(image))
		print("Image count : %d"%img_count)
		if os.path.getsize(image) > 1024*200:
			log_count += 1
			print("Log count : %d"%log_count)
			log_file.write(image + "\n")

log_file.close()