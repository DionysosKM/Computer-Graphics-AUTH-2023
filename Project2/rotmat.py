import numpy as np

def rotmat(theta,u):
    
    ux, uy, uz = u

    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    R = np.array([[cos_theta + ux**2*(1 - cos_theta), ux*uy*(1 - cos_theta) - uz*sin_theta, ux*uz*(1 - cos_theta) + uy*sin_theta],
                           [uy*ux*(1 - cos_theta) + uz*sin_theta, cos_theta + uy**2*(1 - cos_theta), uy*uz*(1 - cos_theta) - ux*sin_theta],
                           [uz*ux*(1 - cos_theta) - uy*sin_theta, uz*uy*(1 - cos_theta) + ux*sin_theta, cos_theta + uz**2*(1 - cos_theta)]])

    return R

 