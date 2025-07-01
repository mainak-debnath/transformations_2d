# transformations_2d

A Python package for performing 2D geometric transformations (translation, scaling, rotation, shearing, reflection) on points and polygons using an object-oriented and immutable design.

## ✨ Features

- Immutable `Point` and `Polygon` classes
- Transformation methods return new instances (non-destructive)
- Supports:
  - Translation
  - Scaling (from origin or custom point)
  - Rotation (around origin or custom point)
  - Shearing (with reference axis)
  - Reflections (across X, Y, origin, or line `y = x`)
- Built-in methods for:
  - String representation (`__str__`)
  - Dictionary serialization (`to_dict`, `from_dict`)

## 📦 Installation

Install via PyPI:

```bash
pip install transformations_2d
```

If you want to install directly from source for development:

```bash
git clone https://github.com/mainak-debnath/transformations_2d.git
cd transformations_2d
pip install .
```

## 🚀 Usage

The package provides Point and Polygon classes, each with methods for various 2D transformations. All transformation methods return a _new_ transformed object, leaving the original unchanged (immutability).

### Point Transformations

```python
from transformations_2d.geometry import Point

# --- Create a point ---
p = Point(10, 20)
print(f"Original Point: {p}")
# → Point(10.00, 20.00)

# --- Access coordinates ---
print(f"x = {p.x}, y = {p.y}")
# → x = 10.0, y = 20.0

# --- Serialize to dict ---
print("Point as dict:", p.to_dict())
# → Point as dict: {'x': 10.0, 'y': 20.0}

# --- Apply transformations ---

# Translate by (5, -3)
translated = p.translate(5, -3)
print(f"Translated (+5, -3): {translated}")
# → Point(15.00, 17.00)

# Scale from origin by (2, 1.5)
scaled = p.scale(2, 1.5)
print(f"Scaled (2x, 1.5x) from origin: {scaled}")
# → Point(20.00, 30.00)

# Scale around custom origin (5, 5)
origin = Point(5, 5)
scaled_custom = p.scale(2, 1.5, origin=origin)
print(f"Scaled (2x, 1.5x) from origin {origin}: {scaled_custom}")
# → Point(15.00, 27.50)

# Rotate 90° counter-clockwise
rotated = p.rotate(90)
print(f"Rotated 90° CCW: {rotated}")
# → Point(-20.00, 10.00)

# Rotate -45° clockwise around custom origin
rotated_custom = p.rotate(-45, origin=origin)
print(f"Rotated -45° CW around {origin}: {rotated_custom}")
# → Point(19.14, 12.07)

# Shear along X-axis with factor 0.5
sheared_x = p.shear_x(0.5)
print(f"Sheared X (0.5): {sheared_x}")
# → Point(20.00, 20.00)

# Shear along Y-axis with factor 0.2
sheared_y = p.shear_y(0.2)
print(f"Sheared Y (0.2): {sheared_y}")
# → Point(10.00, 22.00)

# Reflect across X-axis
reflected_x = p.reflect_x()
print(f"Reflected across X-axis: {reflected_x}")
# → Point(10.00, -20.00)

# Reflect across Y-axis
reflected_y = p.reflect_y()
print(f"Reflected across Y-axis: {reflected_y}")
# → Point(-10.00, 20.00)

# Reflect about the origin
reflected_origin = p.reflect_origin()
print(f"Reflected about origin: {reflected_origin}")
# → Point(-10.00, -20.00)

# Reflect across the line y = x
reflected_xy = p.reflect_xy_line()
print(f"Reflected across y = x: {reflected_xy}")
# → Point(20.00, 10.00)

```

### Polygon Transformations

```python
from transformations_2d.geometry import Point, Polygon

# --- Create a triangle using 3 points ---
p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(0, 5)
triangle = Polygon([p1, p2, p3])

# --- Print original polygon and access its points ---
print(f"Original Triangle: {triangle}")
# Output: Original Triangle: Polygon([(0.00, 0.00), (5.00, 0.00), (0.00, 5.00)])

# --- Access individual point coordinates ---
print("Triangle vertices:")
for pt in triangle.points:
    print(f"({pt.x}, {pt.y})")
# Output:
# (0.0, 0.0)
# (5.0, 0.0)
# (0.0, 5.0)

# --- Serialize to dictionary ---
print("Triangle as dict:", triangle.to_dict())
# Output:
# Triangle as dict: {'points': [{'x': 0.0, 'y': 0.0}, {'x': 5.0, 'y': 0.0}, {'x': 0.0, 'y': 5.0}]}

# --- Apply transformations ---

# Translate by (2, 2)
translated = triangle.translate(2, 2)
print(f"Translated Triangle (by +2,+2): {translated}")
# → Polygon([(2.00, 2.00), (7.00, 2.00), (2.00, 7.00)])

# Scale by 2x from origin
scaled = triangle.scale(2, 2)
print(f"Scaled Triangle (2x from origin): {scaled}")
# → Polygon([(0.00, 0.00), (10.00, 0.00), (0.00, 10.00)])

# Rotate 90° counter-clockwise about origin
rotated = triangle.rotate(90)
print(f"Rotated Triangle (90° CCW): {rotated}")
# → Polygon([(0.00, 0.00), (0.00, 5.00), (-5.00, 0.00)])

# Reflect across the Y-axis
reflected = triangle.reflect_y()
print(f"Reflected Triangle (across Y-axis): {reflected}")
# → Polygon([(0.00, 0.00), (-5.00, 0.00), (0.00, 5.00)])

```

## Development

### 🧪 Running Tests

To run the tests (once implemented in tests/test_geometry.py):

```bash
pip install pytest
pytest tests/
```

## 🤝 Contributing

Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
