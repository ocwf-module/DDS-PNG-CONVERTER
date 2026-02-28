import os
from PIL import Image

# Creating a list of dds files from those in the directory
All_DDS = [f for f in os.listdir('.') if f.endswith('.dds')]

# Creating a folder to save png files
Name_Folder = "PNG"
if not os.path.exists(Name_Folder):
	os.makedirs(Name_Folder)

# Convert and save each dds file in png format
for File in All_DDS:
	IMG = Image.open(File)
	IMG.save(os.path.join(Name_Folder, os.path.splitext(File)[0] + '.png'))
	print(f"[{File}]: Successfully processed")

input('\nThe program has been completed successfully! To close the program, press [Enter]...')
