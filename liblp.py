
# Tools to calculate LP modes
from matplotlib import pyplot as plt
import numpy as np

from scipy.special import jv,kn,kv
from optictools import pyfindpeaks


def jkdiff(m,u,w):
    """ calculate the absolute difference between Jm(u)/Jm+1(u)-Km(w)/Km+1(w)
    useful to determine the branches of LP modes in a step-index fiber

    Args: 
    - m azimuthal number of periods (m=0,1,2,3...)
    - u radial phase constant
    - w radial decay constant

    """
    return np.abs(  jv(m, u)/(u * jv(m+1,u)) - (kn(m,w)/(w*kn(m+1,w))))

def get_branches(m, V, pts=300):
    """ calculate the branches of LPmp, for given m

    Args:
    - m azimuthal number of periods (m=0,1,2,3...)
    - V  V-number, normalized frequency

    """    
    uv = np.linspace(0,V,pts)
    uu,ww = np.meshgrid(uv,uv)
    diff = np.zeros([pts,pts])    
    for i in range(pts):
        for k in range(pts):
            diff[i,k]= jkdiff(m, uu[i,k], ww[i,k])
    return diff,uv

def get_intersects( m,V, epsilon=1e-4, anglepts=500, peakfindpts=20):
    """ calculate the intersects  of a circle of given V-number with the branches of LPmp, for given m

    can be used to determine pairs of u,w for the modes of a given V,m

    Args:
    - m azimuthal number of periods (m=0,1,2,3...)
    - V  V-number, normalized frequency
    - [optional]  epsilon=1e-4, anglepts=500, peakfindpts=20   parameters to determine whether an intersect is 'real'
    """
    angle = np.linspace(epsilon, np.pi/2.0-epsilon,anglepts)
    w = np.sin(angle) * V
    u = np.cos(angle) * V
    pl = pyfindpeaks(peakfindpts, 1./jkdiff( m , u, w),epsilon)
    res = []
    for p in pl:
        res.append( [u[p], w[p]])
    return res

def besselmode(m, u, w, x, y, phioff):
    """ calculate the (unscaled!) field of a bessel mode LP mode

    Args:
    - m azimuthal number of periods (m=0,1,2,3...)
    - u, w  radial phase constant and radial decay constant
    - x, y transverse coordinates
    - phioff: offset angle

    """

    r = np.sqrt( x**2+ y**2)        
    phi = np.arctan2(x,y)
    fak = jv(m,u)/kn(m, w)    
    if r<=1: 
        return jv(m,u*r)*np.cos(m*phi+phioff)
    else:
        return fak*kv(m,w*r)*np.cos(m*phi+phioff)
