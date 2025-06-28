# tests/test_geometry.py
import pytest
from transformations_2d.geometry import Point, Polygon


# --- Point Tests ---
def test_point_creation():
    p = Point(1, 2)
    assert p.x == 1.0
    assert p.y == 2.0


def test_point_repr():
    p = Point(1.234, 5.678)
    assert repr(p) == "Point(x=1.23, y=5.68)"


def test_point_equality():
    p1 = Point(1, 2)
    p2 = Point(1.0, 2.0)
    p3 = Point(1.0000000000000001, 2.0000000000000001)  # Floating point close
    p4 = Point(3, 4)
    assert p1 == p2
    assert p1 == p3
    assert p1 != p4
    assert p1 != "not a point"


def test_point_translate():
    p = Point(10, 20)
    translated_p = p.translate(5, -3)
    assert translated_p == Point(15, 17)
    assert p == Point(10, 20)  # Original point is unchanged (immutability)


def test_point_scale_from_origin():
    p = Point(10, 20)
    scaled_p = p.scale(2, 0.5)
    assert scaled_p == Point(20, 10)


def test_point_scale_from_custom_origin():
    p = Point(10, 20)
    origin = Point(5, 10)
    scaled_p = p.scale(2, 0.5, origin=origin)
    # (10-5)*2 + 5 = 15
    # (20-10)*0.5 + 10 = 15
    assert scaled_p == Point(15, 15)


def test_point_rotate_90_ccw_from_origin():
    p = Point(10, 0)
    rotated_p = p.rotate(90)
    assert rotated_p == Point(0, 10)


def test_point_rotate_180_from_origin():
    p = Point(5, 5)
    rotated_p = p.rotate(180)
    assert rotated_p == Point(-5, -5)


def test_point_rotate_custom_origin():
    p = Point(10, 2)
    origin = Point(5, 2)
    rotated_p = p.rotate(90, origin=origin)
    # Relative to origin: (5, 0)
    # Rotated relative: (0, 5)
    # Absolute: (0+5, 5+2) = (5, 7)
    assert rotated_p == Point(5, 7)


def test_point_shear_x():
    p = Point(10, 20)
    sheared_p = p.shear_x(0.5)  # x' = 10 + 0.5 * 20 = 20
    assert sheared_p == Point(20, 20)


def test_point_shear_x_with_ref_y():
    p = Point(10, 20)
    sheared_p = p.shear_x(0.5, ref_y=10)  # x' = 10 + 0.5 * (20 - 10) = 15
    assert sheared_p == Point(15, 20)


def test_point_shear_y():
    p = Point(10, 20)
    sheared_p = p.shear_y(0.5)  # y' = 20 + 0.5 * 10 = 25
    assert sheared_p == Point(10, 25)


def test_point_shear_y_with_ref_x():
    p = Point(10, 20)
    sheared_p = p.shear_y(0.5, ref_x=5)  # y' = 20 + 0.5 * (10 - 5) = 22.5
    assert sheared_p == Point(10, 22.5)


def test_point_reflect_x_axis():
    p = Point(5, 10)
    reflected_p = p.reflect_x()
    assert reflected_p == Point(5, -10)


def test_point_reflect_x_axis_custom():
    p = Point(5, 10)
    reflected_p = p.reflect_x(axis_y=5)  # Reflection across y=5
    # y' = 2*5 - 10 = 0
    assert reflected_p == Point(5, 0)


def test_point_reflect_y_axis():
    p = Point(5, 10)
    reflected_p = p.reflect_y()
    assert reflected_p == Point(-5, 10)


def test_point_reflect_y_axis_custom():
    p = Point(5, 10)
    reflected_p = p.reflect_y(axis_x=2)  # Reflection across x=2
    # x' = 2*2 - 5 = -1
    assert reflected_p == Point(-1, 10)


def test_point_reflect_origin():
    p = Point(5, 10)
    reflected_p = p.reflect_origin()
    assert reflected_p == Point(-5, -10)


def test_point_reflect_xy_line():
    p = Point(5, 10)
    reflected_p = p.reflect_xy_line()
    assert reflected_p == Point(10, 5)


# --- Polygon Tests ---
def test_polygon_creation():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    poly = Polygon([p1, p2, p3])
    assert len(poly.points) == 3
    assert poly.points[0] == p1


def test_polygon_immutability_of_points_list():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    initial_points = [p1, p2, p3]
    poly = Polygon(initial_points)

    # Modify the original list
    initial_points.append(Point(10, 10))

    # Check that the polygon's internal list was not affected
    assert len(poly.points) == 3


def test_polygon_immutability_of_returned_points():
    p1 = Point(0, 0)
    poly = Polygon([p1])
    retrieved_points = poly.points
    # Attempt to modify a point within the retrieved list (should create a new Point object by Point's design)
    # The list itself is a copy, so modifying it won't affect the polygon's internal list
    retrieved_points.append(Point(5, 5))
    assert len(poly.points) == 1


def test_polygon_equality():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    poly1 = Polygon([p1, p2, p3])
    poly2 = Polygon([Point(0, 0), Point(1, 0), Point(0, 1)])
    poly3 = Polygon([p1, p2])
    assert poly1 == poly2
    assert poly1 != poly3
    assert poly1 != "not a polygon"


def test_polygon_translate():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    poly = Polygon([p1, p2, p3])
    translated_poly = poly.translate(2, 3)
    assert translated_poly == Polygon([Point(2, 3), Point(3, 3), Point(2, 4)])
    assert poly == Polygon([p1, p2, p3])  # Original unchanged


def test_polygon_scale():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    poly = Polygon([p1, p2, p3])
    scaled_poly = poly.scale(2, 3)
    assert scaled_poly == Polygon([Point(0, 0), Point(2, 0), Point(0, 3)])


def test_polygon_rotate():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    poly = Polygon([p1, p2, p3])
    rotated_poly = poly.rotate(90)
    assert rotated_poly == Polygon([Point(0, 0), Point(0, 1), Point(-1, 0)])


def test_polygon_shear_x():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    poly = Polygon([p1, p2, p3])
    sheared_poly = poly.shear_x(0.5)
    assert sheared_poly == Polygon([Point(0, 0), Point(1, 0), Point(0.5, 1)])


def test_polygon_shear_y():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    poly = Polygon([p1, p2, p3])
    sheared_poly = poly.shear_y(0.5)
    assert sheared_poly == Polygon([Point(0, 0), Point(1, 0.5), Point(0, 1)])


def test_polygon_reflect_x():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    poly = Polygon([p1, p2, p3])
    reflected_poly = poly.reflect_x()
    assert reflected_poly == Polygon([Point(0, 0), Point(1, 0), Point(0, -1)])


def test_polygon_reflect_y():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    poly = Polygon([p1, p2, p3])
    reflected_poly = poly.reflect_y()
    assert reflected_poly == Polygon([Point(0, 0), Point(-1, 0), Point(0, 1)])


def test_polygon_reflect_origin():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    poly = Polygon([p1, p2, p3])
    reflected_poly = poly.reflect_origin()
    assert reflected_poly == Polygon([Point(0, 0), Point(-1, 0), Point(0, -1)])


def test_polygon_reflect_xy_line():
    p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
    poly = Polygon([p1, p2, p3])
    reflected_poly = poly.reflect_xy_line()
    assert reflected_poly == Polygon([Point(0, 0), Point(0, 1), Point(1, 0)])


def test_polygon_empty_points_list():
    with pytest.raises(ValueError, match="Polygon must contain at least one point."):
        Polygon([])


def test_polygon_non_point_elements():
    with pytest.raises(
        TypeError, match="All elements in 'points' must be instances of Point."
    ):
        Polygon([Point(0, 0), (1, 1)])
