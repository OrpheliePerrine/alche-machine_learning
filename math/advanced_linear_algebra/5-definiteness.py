#!/usr/bin/env python3
"""Definiteness of a matrix"""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix

    matrix: numpy.ndarray of shape (n, n) whose definiteness
            should be calculated

    Raises:
        TypeError: if matrix is not a numpy.ndarray

    Returns: the string Positive definite, Positive semi-definite,
             Negative semi-definite, Negative definite or Indefinite,
             or None if matrix is invalid or fits no category
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Must be a non-empty square 2D matrix
    if matrix.ndim != 2 or matrix.shape[0] == 0:
        return None
    if matrix.shape[0] != matrix.shape[1]:
        return None

    # Only symmetric matrices are classified
    if not np.allclose(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvalsh(matrix)

    # Tolerance so tiny floating point errors count as zero
    tol = 1e-8 * max(1.0, np.max(np.abs(eigenvalues)))

    if np.all(eigenvalues > tol):
        return "Positive definite"
    if np.all(eigenvalues < -tol):
        return "Negative definite"
    if np.all(eigenvalues >= -tol):
        return "Positive semi-definite"
    if np.all(eigenvalues <= tol):
        return "Negative semi-definite"
    return "Indefinite"
