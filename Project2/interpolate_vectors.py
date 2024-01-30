import math as m
import numpy as np

def interpolate_vectors(p1, p2, V1, V2, xy, dim):
    d = m.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))  
    if dim == 1: 
       y = p1[1]*((p2[0]-xy)/(p2[0]-p1[0]))+p2[1]*((xy-p1[0])/(p2[0]-p1[0]))
       p = [xy,y]
    elif dim == 2:
       x = p1[0]*((p2[1]-xy)/(p2[1]-p1[1]))+p2[0]*((xy-p1[1])/(p2[1]-p1[1]))
       p = [x,xy]
    else:
        print("dimension not supported")
           
    d1 = m.sqrt(((p1[0]-p[0])**2)+((p1[1]-p[1])**2))
    V = (d1/d)*V2 + (1-d1/d)*V1
    return V  