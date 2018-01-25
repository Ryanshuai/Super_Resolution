import argparse
import os
from os.path import join

import torch
from torch.autograd import Variable
import torchvision.transforms as transforms

from util import load_img, save_img

test_input_fold = 'test_data/inter_4/'
test_target_fold = 'test_data/high_resolution_images/'
test_result_fold = 'test_data/result/'

model_parameter_path = 'checkpoint/facades/netG_model_epoch_200.pth'
netG = torch.load(model_parameter_path)

image_filelist = os.listdir(test_input_fold)

transform_list = [transforms.ToTensor(),
                  transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]

transform = transforms.Compose(transform_list)

for image_name in image_filelist:
    img = load_img(test_input_fold + image_name)
    img = transform(img)
    input = Variable(img, volatile=True).view(1, -1, 256, 256)

    if True: # opt.cuda:
        netG = netG.cuda()
        input = input.cuda()

    out = netG(input)
    out = out.cpu()
    out_img = out.data[0]
    if not os.path.exists(test_result_fold):
        os.mkdir(test_result_fold)
    save_img(out_img, test_result_fold + image_name)
