#!/usr/bin/env python3
"""Tests a dll written in c"""

from ctypes import cdll
import os

DLL_PATH_NAME = "../c_lib/simpleMath.so"
if not os.path.isfile(DLL_PATH_NAME):
    raise Exception("dll not found: " + str(DLL_PATH_NAME))

libsomme = cdll.LoadLibrary(DLL_PATH_NAME)
print(f"3  + 5 = {libsomme.sum(3, 5)}")
print(f"10 - 4 = {libsomme.sub(10, 4)}")
