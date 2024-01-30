import numpy as np
import PinHole as PH

def CameraLookingAt(f, cv, cK, cup, p3d):

    cK = cK + cv
    cz = cK / np.linalg.norm(cK)
    t = cup - np.inner(cup, cz) * cz
    cy = t / np.linalg.norm(t)
    cx = np.cross(cy, cz)

    return PH.PinHole(f, cv, cx, cy, cz, p3d)
