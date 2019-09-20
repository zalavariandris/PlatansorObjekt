# -*- coding: utf-8 -*-

from utils import persp, get_files_in_dir
from IPython.core.display import display
from PDF import PDF
from geo import Rectangle

def compose_pdf(files, rectangles, pdf):
    pdf.set_auto_page_break(False, 0)
    pdf.set_font('Courier','B', 6)

    rectangles = list(rectangles)
    n = len(rectangles)
    for i, file_mediabox in enumerate(zip(files, rectangles)):
        file, mediabox = file_mediabox
        # add new page
        pdf.add_page()

        # add image to page
        pdf.image(file, 
            x = mediabox.left, 
            y = mediabox.top, 
            w = mediabox.width, 
            h = mediabox.height)
        
        # define trimbox
        bleed=0.05
        trimbox = mediabox.shrink(margin=bleed)
        pdf.corner_crop_mark(trimbox)
        
        frame_width = 0.25
        if i<n-5 and frame_width>0:
            cover = trimbox.shrink(margin=frame_width)
            if( cover.height>0 and cover.width>0):
                top, left, bottom, right = cover
                pdf.set_fill_color(255,255,255)
                pdf.rect(x = left,
                         y = top, 
                         w = right-left, 
                         h = bottom-top,
                         style="F")
                
            cross_size =  0.25
            if(cover.height>cross_size+bleed and cover.width>cross_size+bleed):               
                # add upper_mark
                pdf.cross(pdf.w/2, pdf.h/2+0.5, cross_size)    
                pdf.cross(pdf.w/2, pdf.h/2-0.5, cross_size)    
                
                # add page number                
                text = "{}".format(pdf.page_no())
                pdf.set_xy(cover.left, cover.top)
                pdf.multi_cell(cover.width, cover.height, 
                    text, align="C");
        else:
            text = "{}".format(pdf.page_no())
            pdf.set_xy(pdf.w-1, pdf.h-1)
            pdf.cell(0,0, 
                text, align="C");
        

    return pdf

from PIL import Image
if __name__ == "__main__":
    files = list(get_files_in_dir("C:/Users/andris/Desktop/00066_stabilized_adjusted"))
    step = int(len(files)/20)
    files = files[::step]
    n = len(files)

    print("create pdf...")
    pdf = PDF(orientation = 'P', unit = 'in', format='A4')
    pdf.line_width = 0
    
    print("create rectangles...")
    image = Image.open(files[0])
    image_rect = Rectangle(0, 0, image.height, image.width)
    page_rect = Rectangle(0, 0, pdf.h, pdf.w)
    print_rect = page_rect.shrink(0.5)
    rect = image_rect.fitIn(print_rect)
    rectangles = [persp(rect, k=400, distance=i*step) for i in range(n)]
    
    print("put images on pdf...")
    compose_pdf(files, rectangles, pdf)

    pdf.output("platasorok.pdf", 'F')
    import os
    os.startfile("platasorok.pdf")
