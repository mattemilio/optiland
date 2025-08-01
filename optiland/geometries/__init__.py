"""This package defines various optical surface geometries used in Optiland,
ranging from simple planes and spheres to complex aspheres and polynomial
surfaces."""

from .base import BaseGeometry
from .biconic import BiconicGeometry
from .chebyshev import ChebyshevPolynomialGeometry
from .even_asphere import EvenAsphere
from .newton_raphson import NewtonRaphsonGeometry
from .odd_asphere import OddAsphere
from .plane import Plane
from .plane_grating import PlaneGrating
from .polynomial import PolynomialGeometry
from .standard import StandardGeometry
from .standard_grating import StandardGratingGeometry
from .toroidal import ToroidalGeometry
from .zernike import ZernikePolynomialGeometry, factorial

__all__ = [
    # From base.py
    "BaseGeometry",
    # From biconic.py
    "BiconicGeometry",
    # From chebyshev.py
    "ChebyshevPolynomialGeometry",
    # From even_asphere.py
    "EvenAsphere",
    # From newton_raphson.py
    "NewtonRaphsonGeometry",
    # From odd_asphere.py
    "OddAsphere",
    # From plane.py
    "Plane",
    # From plane_grating.py
    "PlaneGrating",
    # From polynomial.py
    "PolynomialGeometry",
    # From standard.py
    "StandardGeometry",
    # From standard_grating.py
    "StandardGratingGeometry",
    # From toroidal.py
    "ToroidalGeometry",
    # From zernike.py
    "ZernikePolynomialGeometry",
    "factorial",
]
