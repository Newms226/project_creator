import os
from os import path
import tempfile

def validCheck(directory:str, root = os.curdir):


def exsits(directory:str, root = os.curdir):
    return path.exists(path.join(root, str))


def create(directory:str, root = os.curdir):
    try:
        joined_dir = path.join(root, directory)
        os.mkdir(joined_dir)
        if not exsits(joined_dir): raise IOError
    except FileExistsError:  # TODO handle exception
    except IOError: # TODO

    return joined_dir

def create_temp(director:str, root = os.curdir):

