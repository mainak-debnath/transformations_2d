# transformations_2d

A Python package for performing 2D geometric transformations (translation, scaling, rotation, shearing, reflection) on points and polygons using an object-oriented approach.

## Installation

You can install this package using pip:

```
pip install transformations_2d
```

If you want to install directly from source for development:

```
git clone https://github.com/mainak-debnath/transformations_2d.git
cd transformations_2d
pip install .
```

## Usage

The package provides Point and Polygon classes, each with methods for various 2D transformations. All transformation methods return a _new_ transformed object, leaving the original unchanged (immutability).

### Point Transformations

```
from transformations_2d.geometry import Point

# Create a point
p = Point(x=10, y=20)
print(f"Original Point: {p}")

# --- Translation ---
translated_p = p.translate(tx=5, ty=-3)
print(f"Translated Point: {translated_p}")

# --- Scaling (relative to origin) ---
scaled_p = p.scale(sx=2, sy=1.5)
print(f"Scaled Point (from origin): {scaled_p}")

# --- Scaling around a custom origin ---
origin_point = Point(5, 5)
scaled_p_custom_origin = p.scale(sx=2, sy=1.5, origin=origin_point)
print(f"Scaled Point (from custom origin {origin_point}): {scaled_p_custom_origin}")

# --- Rotation (positive = counter-clockwise) ---
rotated_p = p.rotate(angle_degrees=90)
print(f"Rotated Point (90° CCW from origin): {rotated_p}")

# --- Rotation around custom origin ---
rotated_p_custom_origin = p.rotate(angle_degrees=-45, origin=origin_point)
print(f"Rotated Point (-45° CW from custom origin {origin_point}): {rotated_p_custom_origin}")

# --- Shearing along X-axis ---
sheared_x_p = p.shear_x(sh_x=0.5)
print(f"Sheared X Point (ref y=0): {sheared_x_p}")

# --- Shearing along Y-axis ---
sheared_y_p = p.shear_y(sh_y=0.2)
print(f"Sheared Y Point (ref x=0): {sheared_y_p}")

# --- Reflection across X-axis ---
reflected_x_p = p.reflect_x()
print(f"Reflected Point (across X-axis): {reflected_x_p}")

# --- Reflection across Y-axis ---
reflected_y_p = p.reflect_y()
print(f"Reflected Point (across Y-axis): {reflected_y_p}")

# --- Reflection about the origin ---
reflected_origin_p = p.reflect_origin()
print(f"Reflected Point (about Origin): {reflected_origin_p}")

# --- Reflection across the line Y = X ---
reflected_xy_p = p.reflect_xy_line()
print(f"Reflected Point (across Y = X line): {reflected_xy_p}")

```

### Polygon Transformations

```
from transformations_2d.geometry import Point, Polygon

# --- Create points for a triangle ---
p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(0, 5)

# --- Create a polygon (triangle) ---
triangle = Polygon([p1, p2, p3])
print(f"Original Triangle: {triangle}")

# --- Translate the triangle ---
translated_triangle = triangle.translate(tx=2, ty=2)
print(f"Translated Triangle: {translated_triangle}")

# --- Scale the triangle (relative to origin) ---
scaled_triangle = triangle.scale(sx=2, sy=2)
print(f"Scaled Triangle (from origin): {scaled_triangle}")

# --- Rotate the triangle (90° CCW around origin) ---
rotated_triangle = triangle.rotate(angle_degrees=90)
print(f"Rotated Triangle (90° CCW from origin): {rotated_triangle}")

# --- Reflect the triangle across the Y-axis ---
reflected_y_triangle = triangle.reflect_y()
print(f"Reflected Triangle (across Y-axis): {reflected_y_triangle}")
```

## Development

### Running Tests

To run the tests (once implemented in tests/test_geometry.py):

```
pip install pytest
pytest tests/
```

## Contributing

Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
