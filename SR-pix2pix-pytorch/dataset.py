from os import listdir
from os.path import join

import torch.utils.data as data
import torchvision.transforms as transforms

from util import is_image_file, load_img


def get_training_set():
    train_dir = "train_data/"
    return DatasetFromFolder(train_dir)

def get_test_set():
    test_dir = "test_data/"
    return DatasetFromFolder(test_dir)


class DatasetFromFolder(data.Dataset):
    def __init__(self, image_dir):
        super(DatasetFromFolder, self).__init__()
        self.inter_4_path = join(image_dir, "LR_4")
        self.inter_4_filelist = listdir(self.inter_4_path)

        self.high_resolution_images_path = join(image_dir, "HR")
        self.high_filelist = listdir(self.high_resolution_images_path)

        transform_list = [transforms.ToTensor(),
                          transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]

        self.transform = transforms.Compose(transform_list)

    def __getitem__(self, index):
        # Load Image
        input = load_img(join(self.inter_4_path, self.inter_4_filelist[index]))
        input = self.transform(input)
        target = load_img(join(self.high_resolution_images_path, self.inter_4_filelist[index]))
        target = self.transform(target)

        return input, target

    def __len__(self):
        return len(self.high_filelist)
