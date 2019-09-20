# -*- coding: utf-8 -*-
from geo import Rectangle

def persp(rect: tuple, k:float, distance:float)->tuple:
    top, left, bottom, right = rect
    center = ( (left+right)/2, (top+bottom)/2 )
    factor = 1/(1+distance/k);

    return Rectangle.scale(rect, factor, center)

def get_files_in_dir(dirpath):
    print("get files in folder...", dirpath)
    # get all htlm files
    import os
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
        filepath = os.path.normpath(filepath)
        yield filepath