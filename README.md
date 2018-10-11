# liblp.py

rev 1 - 27.04.2015


# overview

This small toolkit allows to calculate the transverse fiber modes guided in a simple step-index fiber.
Such a fiber is characterized by the _normalized frequency_, V (V-number).




<img src="doc_etc/for_v.png" alt="v-number" width="400"/>

where \lambda_0 is the wavelength, a the core radius and n_co and n_cl are the refractive indeces of the core and the cladding, respectively.

Valid (guided) fiber modes that can be determined by solving the differential equation 

<img src="doc_etc/for_jk.png" alt="relation for bessel functions" width="320"/>

where J_i and K_i are the _i_ - th Bessel functions, and _u_ and _w_ dimensionless, positive numbers fulfilling the condition

<img src="doc_etc/for_uw.png" alt="v-uw" width="290"/>

The branches of the first view modes in the u-v-Plane are shown in the picture below.
<img src="doc_etc/uw_plane.png" alt="first few branches" width="900"/>


# using the toolkit - determining which modes are guided

Using the function **get\_intersects** from liblp, the intersection points of a circle of radius **V** with the mode branches in the u-w-plance can be calculated.

The function looks for branches and returns the intersection coordinates.

Example: for V=6, the modes LP01, LO02, LP11, LP12, LP21, and LP31 are supported.

```from liblp import *
V=6
for m in range(5):
    intersects = get_intersects(m, V)
    print("\nm=%d, # of intersections: %d\n"%(m, len(intersects)))
    for intersect in intersects:
        print("  %s u=%.3f w=%.3f"%(intersect[2], intersect[0], intersect[1]))
```
resulting output:

```
m=0, # of intersections: 2

  LP01 u=2.054 w=5.637
  LP02 u=4.630 w=3.816

m=1, # of intersections: 2

  LP11 u=3.253 w=5.042
  LP12 u=5.750 w=1.713

m=2, # of intersections: 1

  LP21 u=4.342 w=4.141

m=3, # of intersections: 1

  LP31 u=5.352 w=2.712

m=4, # of intersections: 0
```


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
