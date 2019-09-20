# -*- coding: utf-8 -*-

from fpdf import FPDF
from PIL import Image
class PDF(FPDF):
    def cross(self, x: float, y: float, size: float):
        self.line(x-size/2,y, x+size/2, y)#horizontal
        self.line(x,y-size/2,x, y+size/2 )#vertical
    
    def corner_crop_mark(self, rect:tuple, d:float=0.25):
        top, left, bottom, right = rect
        #top left
        self.line(left-d,top,left-d/2, top )#horizontal
        self.line(left,top-d,left, top-d/2 )#vertical
        
        #top right
        self.line(right+d,top,right+d/2, top ) #horizontal
        self.line(right,top-d,right, top-d/2 ) #vertical
        
        #bottom left
        self.line(left-d,bottom,left-d/2, bottom )#horizontal
        self.line(left,bottom+d,left, bottom+d/2 )#vertical
        
        #bottom right
        self.line(right+d,bottom,right+d/2, bottom )#horizontal
        self.line(right,bottom+d,right, bottom+d/2 )#vertical