import numpy as np
from scipy.special import jv,kn, kv
def besselmode(m, u, w, x, y, phioff=0):
    """Calculate the field of a bessel mode LP mode.

    Arguments:
    - m azimuthal number of periods (m=0,1,2,3...)
    - u, w  radial phase constant and radial decay constant
    - x, y transverse coordinates
    - phioff: offset angle, allows to rotate the mode in
              the x-y plane

    """
    xx,yy = np.meshgrid(x,y)
    rr = np.reshape( np.sqrt(xx**2 + yy**2), len(x)*len(y))
    phi = np.reshape( np.arctan2(xx,yy), len(x)*len(y))
    fak = jv(m,u)/kn(m, w)
    res = np.zeros(len(rr))
    indx1 = rr<=1
    res[indx1] = jv(m,u*rr[indx1])*np.cos(m*phi[indx1]+phioff)
    indx2 = rr>1
    res[indx2] = fak * kn(m, w * rr[indx2]) * np.cos(m * phi[indx2] + phioff)
    res = res / np.max(np.abs(res))
    return np.reshape(res, [len(y), len(x)])