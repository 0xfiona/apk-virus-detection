# -*- coding: utf-8 -*-
import os
import subprocess

def disassemble(frompath,filename,topath, num, start=0):
    fullTopath = os.path.join(topath, filename)
    command = "apktool d " + frompath + " -o " + fullTopath + " -f "
    subprocess.call(command, shell=True)

