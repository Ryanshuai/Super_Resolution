import os
from os.path import join

images_fold = 'train_data/HR/'

for image_name in os.listdir(images_fold):
    old_path = join(images_fold, image_name)
    new_path = join(images_fold, image_name[5:])
    os.rename(old_path, new_path)
    print('change ',image_name , ' to ', image_name[5:])




