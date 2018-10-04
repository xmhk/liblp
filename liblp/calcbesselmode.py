import numpy as np
from scipy.special import jv,kn, kv
def besselmode(m, u, w, x, y, phioff=0):
    """ calculate the field of a bessel mode LP mode

    Args:
    - m azimuthal number of periods (m=0,1,2,3...)
    - u, w  radial phase constant and radial decay constant
    - x, y transverse coordinates
    - phioff: offset angle

    """

    #r = np.sqrt( x**2+ y**2)
    xx,yy = np.meshgrid(x,y)
    #yy = np.meshgrid(y,y)
    rr = np.reshape( np.sqrt(xx**2 + yy**2), len(x)*len(y))
    phi = np.reshape( np.arctan2(xx,yy), len(x)*len(y))
    #phi = np.arctan2(x,y)
    fak = jv(m,u)/kn(m, w)
    #if r<=1:
    #    return jv(m,u*r)*np.cos(m*phi+phioff)
    #else:
    #    return fak*kv(m,w*r)*np.cos(m*phi+phioff)


    res = np.zeros(len(rr))
    indx1 = rr<=1
    res[indx1] = jv(m,u*rr[indx1])*np.cos(m*phi[indx1]+phioff)
    indx2 = rr>1
    #res[indx2] = fak*kv(m,w*rr[indx2])*np.cos(m*phi[indx2]+phioff)
    res[indx2] = fak * kn(m, w * rr[indx2]) * np.cos(m * phi[indx2] + phioff)
    res = res / np.max(np.abs(res))
    return np.reshape(res, [len(y), len(x)])