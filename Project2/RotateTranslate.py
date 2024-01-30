import numpy as np
import rotmat


def RotateTranslate(cp, theta, u, t):
    
    R = rotmat.rotmat(theta, u)
    cq = np.zeros(cp.shape)

    if cp.ndim == 1:
        cq = R @ cp.transpose()
    else:    
        for i in range(len(cp)):
            cq[i] = R @ cp[i].transpose()

    cq = cq + t
    return cq

