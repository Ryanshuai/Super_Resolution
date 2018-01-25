import shutil
import os
from os import listdir
from os.path import join
from util import is_image_file



def not_png_file(filename):
    return not any(filename.endswith(extension) for extension in [".png"])



father_fold = os.getcwd()
original_path = join(father_fold, "original")
new_fold = join(father_fold, "high_resolution_images")

i=0
for cas in os.listdir(original_path):
    cas_path = join(original_path, cas)
    for siz in os.listdir(cas_path):
        siz_path = join(cas_path,siz)
        for resul in os.listdir(siz_path):
            resul_path = join(siz_path, resul)
            if len(os.listdir(resul_path)) != 0:
                for imag in os.listdir(resul_path):
                    imag_path = join(resul_path, imag)
                    if is_image_file(imag_path):
                        print(imag_path)
                        assert not_png_file(imag_path)
                        shutil.copyfile(imag_path, new_fold + '/high_' + str(i) + '.jpg')
                        i += 1
                        print(i)

