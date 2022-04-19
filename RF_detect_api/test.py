# -*- coding: utf-8 -*-
"""
反汇编良性软件、恶意软件、测试软件　　　
"""
import sys
import batch_disasseble
import bytecode_extract
import n_gram
import RF_usage
import getfeature

test_root = sys.argv[1]
filename = sys.argv[2]
batch_disasseble.disassemble(test_root,filename,"/home/group9/smalis/test", 600)

testwroot = "/home/group9/smalis/test"
f = bytecode_extract.DataFile("/home/group9/data.csv")
bytecode_extract.collect(testwroot,filename, 2,f)
f.close()

n_gram.gram()
getfeature.get()
RF_usage.RF()
