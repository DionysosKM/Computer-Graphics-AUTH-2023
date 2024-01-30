import numpy as np
import rotmat
import RotateTranslate as RT
import RenderObject as RO
import matplotlib.pyplot


verts3d = np.load("h2.npy", allow_pickle=True).tolist()['verts3d'].T
vcolors = np.load("h2.npy", allow_pickle=True).tolist()['vcolors']
faces = np.load("h2.npy", allow_pickle=True).tolist()['faces']
u  = np.load("h2.npy", allow_pickle=True).tolist()['u']
cK = np.load("h2.npy", allow_pickle=True).tolist()['c_lookat'].T
cup = np.load("h2.npy", allow_pickle=True).tolist()['c_up'].T
cv = np.load("h2.npy", allow_pickle=True).tolist()['c_org'].T
t1 = np.load("h2.npy", allow_pickle=True).tolist()['t_1']
t2 = np.load("h2.npy", allow_pickle=True).tolist()['t_2']
phi = np.load("h2.npy", allow_pickle=True).tolist()['phi']

Rows = Columns = 512
H = W = 15
f = 70

img =  RO.RenderObject(verts3d,faces,vcolors,H,W,Rows,Columns,f,cv,cK,cup)
matplotlib.pyplot.figure(1)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.savefig('0.png')
matplotlib.pyplot.ion()

verts3d = RT.RotateTranslate(verts3d, 0, u, t1)
img =  RO.RenderObject(verts3d,faces,vcolors,H,W,Rows,Columns,f,cv,cK,cup)
matplotlib.pyplot.figure(2)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.savefig('1.png')
matplotlib.pyplot.ion()

verts3d = RT.RotateTranslate(verts3d, phi, u, [0,0,0])
img =  RO.RenderObject(verts3d,faces,vcolors,H,W,Rows,Columns,f,cv,cK,cup)
matplotlib.pyplot.figure(3)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.savefig('2.png')
matplotlib.pyplot.ion()

verts3d = RT.RotateTranslate(verts3d, 0, u, t2)
img =  RO.RenderObject(verts3d,faces,vcolors,H,W,Rows,Columns,f,cv,cK,cup)
matplotlib.pyplot.figure(4)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.savefig('3.png')
matplotlib.pyplot.ion()

breakpoint