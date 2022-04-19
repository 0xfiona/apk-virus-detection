# -*- coding: utf-8 -*-
from infrastructure.ware import Ware
import os

def collect(rootdir,filename,isMalware,f):
    ware = filename
    warePath = os.path.join(rootdir, ware)
    ware = Ware(warePath, isMalware)
    ware.extractFeature(f)
        

        




