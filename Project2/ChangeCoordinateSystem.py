import numpy as np

def ChangeCoordinateSystem(cp,R,c0):
    
    dp = np.zeros((len(cp),3))
    
    if cp.ndim == 1:
        cp = cp - c0
        dp = R @ cp.transpose()
    else:    
        for i in range(len(cp)):
            cp[i] = cp[i] - c0
            a = R @cp[i].T
            dp[i] = (R @ cp[i].T).T

    return dp        
