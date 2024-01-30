import numpy as np
import render 
import CameraLookingAt as CLA
import rasterize

def RenderObject(p3d,faces,vcolors,H,W,Rows,Columns,f,cv,cK,cup):
    
    p2d, depth = CLA.CameraLookingAt(f, cv, cK, cup, p3d) 
    n2d = rasterize.rasterize(p2d.T, Rows, Columns, H, W)
    n2d = n2d.astype(int)


    return render.render(n2d, vcolors, faces, depth, "gouraud")
