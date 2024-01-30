import numpy as np
import ChangeCoordinateSystem as CCS

def PinHole(f,cv,cx,cy,cz,p3d):
    
    R = np.stack((cx, cy, cz))
    p3d = CCS.ChangeCoordinateSystem(p3d, R, cv)
    depth = p3d[:,2]
    xp = (f/depth) * p3d[:,0]
    yp = (f/depth) * p3d[:,1]
    p2d = np.stack((xp,yp))

    return p2d, depth
