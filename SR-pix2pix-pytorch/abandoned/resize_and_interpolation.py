import shutil
import os
from os import listdir
from os.path import join
from PIL import Image

father_fold = os.getcwd()
train_data = join(father_fold, "train_data")
interpolation_image_path = join(train_data, "inter_4")
high_resolution_image_path = join(train_data, "high_resolution_images")

i = 0
for image in listdir(high_resolution_image_path):
    original_path = join(high_resolution_image_path, image)
    im = Image.open(original_path)

    im = im.resize((192, 192))  #768/4
    im = im.resize((768, 768), Image.BICUBIC) #192*4

    new_path = interpolation_image_path + '/inter_' + image[5:]
    im.save(new_path)
    print(original_path + '-->' + new_path)




