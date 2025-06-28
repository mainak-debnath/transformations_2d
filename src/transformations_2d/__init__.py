# src/transformations/__init__.py

# Import the core classes from geometry.py
from .geometry import Point, Polygon

# Define what gets imported when someone does 'from transformations_2d import *'
__all__ = ["Point", "Polygon"]

# You could also add package-level documentation here
"""
A Python package for 2D geometric transformations.

Provides:
- Point: A class to represent 2D points and perform transformations.
- Polygon: A class to represent polygons (collections of points) and perform transformations.
"""
