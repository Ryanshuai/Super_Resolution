from os import listdir
from os.path import join

import torch.utils.data as data
import torchvision.transforms as transforms

from util import is_image_file, load_img


class DatasetFromFolder(data.Dataset):
    def __init__(self, image_dir):
        super(DatasetFromFolder, self).__init__()
        self.inter_4_path = join(image_dir, "inter_4")
        self.inter_4_filelist = listdir(self.inter_4_path)

        self.high_resolution_images_path = join(image_dir, "high_resolution_images")
        self.high_filelist = listdir(self.high_resolution_images_path)

        transform_list = [transforms.ToTensor(),
                          transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]

        self.transform = transforms.Compose(transform_list)

    def __getitem__(self, index):
        # Load Image
        high_file = 'high_'+self.inter_4_filelist[index][6:]

        input = load_img(join(self.inter_4_path, self.inter_4_filelist[index]))
        input = self.transform(input)
        target = load_img(join(self.high_resolution_images_path, high_file))
        target = self.transform(target)

        return input, target

    def __len__(self):
        return len(self.high_filelist)
