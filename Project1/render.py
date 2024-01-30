import numpy as np
import shade_triangle as shade

def render(verts2d, vcolors, faces, depth, shade_t):
    L = len(verts2d)
    K = len(faces)
    D = np.zeros((K,3))
    for i in range(K):
        D[i][0] = depth[faces[i][0]]
        D[i][1] = depth[faces[i][1]]
        D[i][2] = depth[faces[i][2]]
    D = np.sum(D, axis=1)
    D = np.argsort(D)
    faces = faces[D]
    vertices = [0,0,0]
    vcolorst = [0,0,0]
    img = np.ones((512,512,3))
    for i in range(K):
        vertices = [verts2d[faces[K-1-i][0]], verts2d[faces[K-1-i][1]], verts2d[faces[K-1-i][2]]]
        vcolorst = [vcolors[faces[K-1-i][0]], vcolors[faces[K-1-i][1]], vcolors[faces[K-1-i][2]]] 
        img = shade.shade_triangle(img,vertices,vcolorst,shade_t)  
    return img  