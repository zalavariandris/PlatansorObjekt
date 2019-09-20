# -*- coding: utf-8 -*-

from utils import persp, get_files_in_dir
from PIL import Image
from IPython.core.display import display

def compose_images(pictures, rectangles, canvas):    
    for picture, rect in zip(pictures, rectangles):
        top, left, bottom, right = rect
        image = picture.resize( ( int(right-left), int(bottom-top) ), resample=Image.BICUBIC)
        canvas.paste(image, (int(left), int(top)) )

    return canvas

if __name__ == "__main__":
    files = list(get_files_in_dir("C:/Users/andris/Desktop/00066_stabilized_adjusted"))
    n = len(files)
    step = int(n/100)
    files = files[::step]

    print("create canvas...")
    canvas = Image.new("RGB", Image.open(files[0]).size, color="black")
    
    print("create rectangles...")
    rect = (0,0,canvas.height, canvas.width) 
    rectangles = [persp(rect, k=400, distance=i*step) for i in range(n)]
    
    print("composing images...")
    images = (Image.open(file) for file in files)
    compose_images(images, rectangles, canvas)

    canvas.show()