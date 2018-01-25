import os
from PIL import Image
from os.path import join

father_fold = os.getcwd()
train_data = join(father_fold, "train_data")
interpolation_image_path = join(train_data, "inter_4")
high_resolution_image_path = join(train_data, "high_resolution_images")

for image_path in os.listdir(high_resolution_image_path):
    im_path = join(high_resolution_image_path, image_path)
    im = Image.open(im_path)
    print(im.size)
    assert im.size == (768, 768)

