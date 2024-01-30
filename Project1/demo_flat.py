import numpy as np
import matplotlib.pyplot
import render

verts2d = np.load("h1.npy", allow_pickle=True).tolist()['verts2d']
vcolors = np.load("h1.npy", allow_pickle=True).tolist()['vcolors']
faces = np.load("h1.npy", allow_pickle=True).tolist()['faces']
depth = np.load("h1.npy", allow_pickle=True).tolist()['depth']

img = render.render(verts2d, vcolors, faces, depth, "flat")
img = np.rot90(img)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.savefig('flats.png')
matplotlib.pyplot.show()