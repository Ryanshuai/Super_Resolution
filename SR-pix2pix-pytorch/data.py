import os
from os.path import join

from dataset import DatasetFromFolder

father_fold = os.getcwd()

def get_training_set():
    train_dir = join(father_fold, "train_data")

    return DatasetFromFolder(train_dir)


def get_test_set(root_dir):
    test_dir = join(root_dir, "test")

    return DatasetFromFolder(test_dir)