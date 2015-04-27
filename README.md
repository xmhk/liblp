# liblp.py

rev 1 - 27.04.2015

## besselmode(m, u, w, x, y, phioff)

        calculate the (unscaled!) field of a bessel mode LP mode
        
        Args:
        - m azimuthal number of periods (m=0,1,2,3...)
        - u, w  radial phase constant and radial decay constant
        - x, y transverse coordinates
        - phioff: offset angle
    
## get_branches(m, V, pts=300)
        calculate the branches of LPmp, for given m
        
        Args:
        - m azimuthal number of periods (m=0,1,2,3...)
        - V  V-number, normalized frequency
    
## get\_intersects(m, V, epsilon=0.0001, anglepts=500, peakfindpts=20)
        calculate the intersects  of a circle of given V-number with the branches of LPmp, for given m
        
        can be used to determine pairs of u,w for the modes of a given V,m
        
        Args:
        - m azimuthal number of periods (m=0,1,2,3...)
        - V  V-number, normalized frequency
        - [optional]  epsilon=1e-4, anglepts=500, peakfindpts=20   parameters to determine whether an intersect is 'real'
    
## jkdiff(m, u, w)
        calculate the absolute difference between Jm(u)/Jm+1(u)-Km(w)/Km+1(w)
        useful to determine the branches of LP modes in a step-index fiber
        
        Args: 
        - m azimuthal number of periods (m=0,1,2,3...)
        - u radial phase constant
        - w radial decay constant
