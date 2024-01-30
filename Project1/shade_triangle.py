import numpy as np
import shade_triangle as shade
import flat 
import gouraud

def shade_triangle(canvas,vertices,vcolors,shade_t):
    if shade_t == "flat":
        return flat.flats(canvas, vertices, vcolors)   
    elif shade_t == "gouraud":
        return gouraud.Gourauds(canvas, vertices, vcolors)
    else:
        print("shade_t not supported")