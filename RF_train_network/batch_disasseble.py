# -*- coding: utf-8 -*-
"""
反汇编良性软件、恶意软件、测试软件　　　
"""

import os
import subprocess

def disassemble(frompath, topath, num, start=0):
    files = os.listdir(frompath)
    files = files[start:num]
    total = len(files)
    j = 1
    for i, file in enumerate(files):
        fullFrompath = os.path.join(frompath, file)
        fullTopath = os.path.join(topath, file)
        bool = fullFrompath.endswith(".DS_Store")
        if bool:
            total = total - 1
            continue
        command = ".\\apktool d " + fullFrompath + " -o " + fullTopath
        subprocess.call(command, shell=True)
        print("已反汇编", j, "个应用")
        print("百分比为：",j * 100 / total, "%")
        j += 1



# 反汇编正常软件样本
kind_root = "E:\\virus\\normal"
disassemble(kind_root, "./smalis/kind", 1000)
# nor_num = get_file_num(kind_root, 600)

# 反汇编恶意软件样本
virus_root = "E:\\virus\\virussample"
disassemble(virus_root,"./smalis/malware", 1000)
# virus_num = get_file_num(virus_root, 600)

# 反汇编白测试软件样本
test_root = "./bit/testAndroid/white"
disassemble(test_root,"./smalis/test/white", 600)


# 反汇编黑测试软件样本
test_root = "./bit/testAndroid/black"
disassemble(test_root,"./smalis/test/black", 600)