from ctypes import cdll
import pytest
import os

DLL_PATH_NAME = "./c_lib/simpleMath.so"

@pytest.mark.unit
def test_dll_sum():
    if not os.path.isfile(DLL_PATH_NAME):
        raise Exception("dll not found: " + str(DLL_PATH_NAME))

    libsomme = cdll.LoadLibrary(DLL_PATH_NAME)
    assert (
        libsomme.sum(3, 5) == 8
    ), "Sould be 8"

@pytest.mark.unit
def test_dll_sub():
    if not os.path.isfile(DLL_PATH_NAME):
        raise Exception("dll not found: " + str(DLL_PATH_NAME))

    libsomme = cdll.LoadLibrary(DLL_PATH_NAME)
    assert (
        libsomme.sub(10, 4) == 6
    ), "Sould be 6"
