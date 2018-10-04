import numpy as np
from .auxiliary import pyfindpeaks
from scipy.special import jv,kn

def jkdiff(m,u,w):
    """Calculate the absolute difference diff = |Jm(u)/Jm+1(u)-Km(w)/Km+1(w)|.

    Can be used to determine the branches of LP modes in a step-index fiber.

    Arguments:

        * m azimuthal number of periods (m=0,1,2,3...)
        * u radial phase constant
        * w radial decay constant

    Returns:

        * diff - Difference

    """
    return np.abs(  jv(m, u)/(u * jv(m+1,u)) - (kn(m,w)/(w*kn(m+1,w))))


def calc_jkdiff_matrix(m, V, pts=300):
    """ calculate the Difference
        diff = |Jm(u)/Jm+1(u)-Km(w)/Km+1(w)|
        for a given m for a matrix
        [0..V] x [0..V] with pts x pts values.

    Arguments:

        - m: azimuthal number of periods (m=0,1,2,3...)
        - V:  V-number, normalized frequency

    Optional Arguments:

        - pts: number of grid points for each of the two
               axes of the matrix

    Returns:

        - jkdiffmatrix
        - uv : u vector (=w vector)
    """
    uv = np.linspace(0, V, pts)
    uu, ww = np.meshgrid(uv, uv)
    uu2 = np.reshape(uu, pts * pts)
    ww2 = np.reshape(ww, pts * pts)
    diff = jkdiff(m, uu2, ww2)
    diff = np.reshape(diff, [pts, pts])
    return diff, uv

def get_intersects(m, V, anglepts=500, peakfindpts=5, maxjkdiff=1e-2):
    """Calculate the intersects of the V-circle with the branches of LPmp for given m

    Arguments:

        - m azimuthal number of periods (m=0,1,2,3...)
        - V  V-number, normalized frequency

    Optional arguments:
        - anglepts: number of points for the circle (default=500)
        - peakfindpts: the !!!!!!!!!
           !!!!!!!!!!!!!
           !!!!!!!!!!!!
           !!!!!!!parameters to determine whether an intersect is 'real'
    """
    epsi = 1e-5

    angle = np.linspace(np.pi/2.0-epsi, epsi, anglepts)
    w = np.sin(angle) * V
    u = np.cos(angle) * V
    pl = pyfindpeaks(peakfindpts, 1./jkdiff( m , u, w), 1./maxjkdiff)
    res = []
    for ii,p in enumerate(pl):
        res.append( [u[p], w[p],"LP%d%d"%(m,ii+1)])
    return res


