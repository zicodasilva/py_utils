"""
Useful operations that have been consistently used during my MSc project.

@author: Zico da Silva
"""
from typing import Union
import numpy as np
import sympy as sp


def rot_x(x: Union[float, np.ndarray, sp.Expr]) -> Union[np.ndarray, sp.Matrix]:
    """Generates a rotation matrix from an angle rotated around the x-axis.

    Args:
        x: the angle of rotation. Either a `numpy` or `sympy` expression.

    Returns:
        Rotation matrix. Either a `numpy` or `sympy` array.
    """
    if isinstance(x, sp.Expr):
        c = sp.cos(x)
        s = sp.sin(x)
        func = sp.Matrix
    else:
        c = np.cos(x)
        s = np.sin(x)
        func = np.array
    return func([[1, 0, 0], [0, c, s], [0, -s, c]])


def rot_y(y: Union[float, np.ndarray, sp.Expr]) -> Union[np.ndarray, sp.Matrix]:
    """Generates a rotation matrix from an angle rotated around the y-axis.

    Args:
        y: the angle of rotation. Either a `numpy` or `sympy` expression.

    Returns:
        Rotation matrix. Either a `numpy` or `sympy` array.
    """
    if isinstance(y, sp.Expr):
        c = sp.cos(y)
        s = sp.sin(y)
        func = sp.Matrix
    else:
        c = np.cos(y)
        s = np.sin(y)
        func = np.array
    return func([[c, 0, -s], [0, 1, 0], [s, 0, c]])


def rot_z(z: Union[float, np.ndarray, sp.Expr]) -> Union[np.ndarray, sp.Matrix]:
    """Generates a rotation matrix from an angle rotated around the z-axis.

    Args:
        z: the angle of rotation. Either a `numpy` or `sympy` expression.

    Returns:
        Rotation matrix. Either a `numpy` or `sympy` array.
    """
    if isinstance(z, sp.Expr):
        c = sp.cos(z)
        s = sp.sin(z)
        func = sp.Matrix
    else:
        c = np.cos(z)
        s = np.sin(z)
        func = np.array
    return func([[c, s, 0], [-s, c, 0], [0, 0, 1]])
