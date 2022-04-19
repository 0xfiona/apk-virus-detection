# -*- coding: utf-8 -*-

import os


def get_file_num1(frompath, num, start=0):
    files = os.listdir(frompath)
    files = files[start:num]
    total = len(files)
    for i, file in enumerate(files):
        fullFrompath = os.path.join(frompath, file)
        bool = fullFrompath.endswith(".DS_Store")
        if bool:
            total = total - 1
    return total


kind_root = "E:\\virus\\normal"
nor_num = get_file_num1(kind_root, 1000)

virus_root = "E:\\virus\\virussample"
virus_num = get_file_num1(virus_root, 1000)

test_root = "./bit/testAndroid/white"
white_num = get_file_num1(test_root, 600)
