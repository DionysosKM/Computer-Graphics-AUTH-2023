import numpy as np

def rasterize(p2d, Rows, Columns, H, W):
    
    n2d = np.zeros((len(p2d), 2))
    w_scale = Rows / H
    h_scale = Columns / W

    for i in range(len(p2d)):
        n2d[i,0] = np.around((p2d[i,0] + (H/2)) * h_scale)
        n2d[i,1] = np.around((p2d[i,1] + (W/2)) * w_scale)

    return n2d