# src/transformations/geometry.py
import math
from typing import List, Union


class Point:
    """
    Represents a 2D point (x, y) and provides methods for geometric transformations.
    All transformation methods return a new Point object, ensuring immutability.
    """

    def __init__(self, x: Union[int, float], y: Union[int, float]):
        """
        Initializes a Point object.

        Args:
            x (Union[int, float]): The x-coordinate of the point.
            y (Union[int, float]): The y-coordinate of the point.
        """
        self._x = float(x)  # Store as float for consistent calculations
        self._y = float(y)

    @property
    def x(self) -> float:
        """The x-coordinate of the point."""
        return self._x

    @property
    def y(self) -> float:
        """The y-coordinate of the point."""
        return self._y

    def __repr__(self) -> str:
        """
        Returns a string representation of the Point object for debugging.
        """
        return f"Point(x={self.x:.2f}, y={self.y:.2f})"

    def __eq__(self, other: object) -> bool:
        """
        Compares two Point objects for equality using a tolerance for floating-point numbers.
        Added abs_tol for robust comparison, especially for values near zero.
        """
        if not isinstance(other, Point):
            return NotImplemented
        # Fix: Increase absolute tolerance slightly for more robust comparison with floating point results
        return math.isclose(self.x, other.x, abs_tol=1e-7) and math.isclose(
            self.y, other.y, abs_tol=1e-7
        )

    # --- Basic Vector Operations (Optional, but good for completeness) ---
    def __add__(self, other: "Point") -> "Point":
        """Performs vector addition (self + other)."""
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        """Performs vector subtraction (self - other)."""
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: Union[int, float]) -> "Point":
        """Performs scalar multiplication (self * scalar)."""
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: Union[int, float]) -> "Point":
        """Performs reverse scalar multiplication (scalar * self)."""
        return self.__mul__(scalar)

    # --- Geometric Transformations ---

    def translate(self, tx: Union[int, float], ty: Union[int, float]) -> "Point":
        """
        Translates the point by (tx, ty).

        Args:
            tx (Union[int, float]): The translation distance along the x-axis.
            ty (Union[int, float]): The translation distance along the y-axis.
        Returns:
            Point: A new Point object representing the translated point.
        """
        return Point(self.x + tx, self.y + ty)

    def scale(
        self, sx: Union[int, float], sy: Union[int, float], origin: "Point" = None
    ) -> "Point":
        """
        Scales the point by (sx, sy) relative to an origin point.

        Args:
            sx (Union[int, float]): The scaling factor along the x-axis.
            sy (Union[int, float]): The scaling factor along the y-axis.
            origin (Point, optional): The origin point for scaling. If None, scales
                                      relative to (0,0). Defaults to None.
        Returns:
            Point: A new Point object representing the scaled point.
        """
        if origin is None:
            origin = Point(0, 0)

        # Translate point to origin
        translated_x = self.x - origin.x
        translated_y = self.y - origin.y

        # Apply scaling
        scaled_x = translated_x * sx
        scaled_y = translated_y * sy

        # Translate back from origin
        return Point(scaled_x + origin.x, scaled_y + origin.y)

    def rotate(
        self, angle_degrees: Union[int, float], origin: "Point" = None
    ) -> "Point":
        """
        Rotates the point by a given angle (in degrees) around an origin point.
        Positive angle indicates counter-clockwise rotation.

        Args:
            angle_degrees (Union[int, float]): The rotation angle in degrees.
            origin (Point, optional): The origin point for rotation. If None, rotates
                                      around (0,0). Defaults to None.
        Returns:
            Point: A new Point object representing the rotated point.
        """
        if origin is None:
            origin = Point(0, 0)

        angle_radians = math.radians(angle_degrees)
        cos_angle = math.cos(angle_radians)
        sin_angle = math.sin(angle_radians)

        # Translate point to origin
        px = self.x - origin.x
        py = self.y - origin.y

        # Apply rotation matrix:
        # x_new = x * cos(theta) - y * sin(theta)
        # y_new = x * sin(theta) + y * cos(theta)
        rotated_x = px * cos_angle - py * sin_angle
        rotated_y = px * sin_angle + py * cos_angle

        # Translate back from origin
        return Point(rotated_x + origin.x, rotated_y + origin.y)

    def shear_x(self, sh_x: Union[int, float], ref_y: Union[int, float] = 0) -> "Point":
        """
        Shears the point along the X-axis based on a shear factor and a reference y-coordinate.

        Args:
            sh_x (Union[int, float]): The shear factor along the x-axis.
            ref_y (Union[int, float], optional): The y-coordinate of the reference line (y=ref_y).
                                                 Points on this line are fixed during shearing.
                                                 Defaults to 0 (x-axis).
        Returns:
            Point: A new Point object representing the sheared point.
        """
        # x' = x + sh_x * (y - ref_y)
        # y' = y
        new_x = self.x + sh_x * (self.y - ref_y)
        return Point(new_x, self.y)

    def shear_y(self, sh_y: Union[int, float], ref_x: Union[int, float] = 0) -> "Point":
        """
        Shears the point along the Y-axis based on a shear factor and a reference x-coordinate.

        Args:
            sh_y (Union[int, float]): The shear factor along the y-axis.
            ref_x (Union[int, float], optional): The x-coordinate of the reference line (x=ref_x).
                                                 Points on this line are fixed during shearing.
                                                 Defaults to 0 (y-axis).
        Returns:
            Point: A new Point object representing the sheared point.
        """
        # x' = x
        # y' = y + sh_y * (x - ref_x)
        new_y = self.y + sh_y * (self.x - ref_x)
        return Point(self.x, new_y)

    def reflect_x(self, axis_y: Union[int, float] = 0) -> "Point":
        """
        Reflects the point across a horizontal line (y = axis_y).

        Args:
            axis_y (Union[int, float], optional): The y-coordinate of the reflection axis.
                                                  Defaults to 0 (reflects across the x-axis).
        Returns:
            Point: A new Point object representing the reflected point.
        """
        # y_reflected = axis_y - (y - axis_y) = 2 * axis_y - y
        return Point(self.x, 2 * axis_y - self.y)

    def reflect_y(self, axis_x: Union[int, float] = 0) -> "Point":
        """
        Reflects the point across a vertical line (x = axis_x).

        Args:
            axis_x (Union[int, float], optional): The x-coordinate of the reflection axis.
                                                  Defaults to 0 (reflects across the y-axis).
        Returns:
            Point: A new Point object representing the reflected point.
        """
        # x_reflected = axis_x - (x - axis_x) = 2 * axis_x - x
        return Point(2 * axis_x - self.x, self.y)

    def reflect_origin(self) -> "Point":
        """
        Reflects the point about the origin (0,0).

        Returns:
            Point: A new Point object representing the reflected point.
        """
        return Point(-self.x, -self.y)

    def reflect_xy_line(self) -> "Point":
        """
        Reflects the point across the line y = x.

        Returns:
            Point: A new Point object representing the reflected point.
        """
        return Point(self.y, self.x)


class Polygon:
    """
    Represents a 2D polygon as an ordered list of Point objects.
    All transformation methods return a new Polygon object, ensuring immutability.
    """

    def __init__(self, points: List[Point]):
        """
        Initializes a Polygon object.

        Args:
            points (List[Point]): An ordered list of Point objects that form the polygon.
                                  Must contain at least two points.
        Raises:
            TypeError: If any element in 'points' is not an instance of Point.
            ValueError: If 'points' list is empty.
        """
        if not all(isinstance(p, Point) for p in points):
            raise TypeError("All elements in 'points' must be instances of Point.")
        if not points:
            raise ValueError("Polygon must contain at least one point.")
        self._points = points[
            :
        ]  # Store a shallow copy to maintain internal list integrity

    @property
    def points(self) -> List[Point]:
        """
        Returns a list of points forming the polygon.
        A copy of the internal list is returned to prevent external modification.
        """
        return self._points[:]

    def __repr__(self) -> str:
        """
        Returns a string representation of the Polygon object.
        """
        points_repr = ", ".join(str(p) for p in self._points)
        return f"Polygon([{points_repr}])"

    def __eq__(self, other: object) -> bool:
        """
        Compares two Polygon objects for equality by comparing their points in order.
        """
        if not isinstance(other, Polygon):
            return NotImplemented
        if len(self.points) != len(other.points):
            return False
        return all(p1 == p2 for p1, p2 in zip(self.points, other.points))

    # --- Geometric Transformations for Polygon ---
    # These methods apply the corresponding Point transformation to each vertex
    # and return a new Polygon instance.

    def translate(self, tx: Union[int, float], ty: Union[int, float]) -> "Polygon":
        """Translates all vertices of the polygon by (tx, ty)."""
        translated_points = [p.translate(tx, ty) for p in self._points]
        return Polygon(translated_points)

    def scale(
        self, sx: Union[int, float], sy: Union[int, float], origin: Point = None
    ) -> "Polygon":
        """Scales all vertices of the polygon around an origin."""
        scaled_points = [p.scale(sx, sy, origin) for p in self._points]
        return Polygon(scaled_points)

    def rotate(
        self, angle_degrees: Union[int, float], origin: Point = None
    ) -> "Polygon":
        """Rotates all vertices of the polygon by a given angle around an origin."""
        rotated_points = [p.rotate(angle_degrees, origin) for p in self._points]
        return Polygon(rotated_points)

    def shear_x(
        self, sh_x: Union[int, float], ref_y: Union[int, float] = 0
    ) -> "Polygon":
        """Shears all vertices of the polygon along the X-axis."""
        sheared_points = [p.shear_x(sh_x, ref_y) for p in self._points]
        return Polygon(sheared_points)

    def shear_y(
        self, sh_y: Union[int, float], ref_x: Union[int, float] = 0
    ) -> "Polygon":
        """Shears all vertices of the polygon along the Y-axis."""
        sheared_points = [p.shear_y(sh_y, ref_x) for p in self._points]
        return Polygon(sheared_points)

    def reflect_x(self, axis_y: Union[int, float] = 0) -> "Polygon":
        """Reflects all vertices of the polygon across a horizontal line."""
        reflected_points = [p.reflect_x(axis_y) for p in self._points]
        return Polygon(reflected_points)

    def reflect_y(self, axis_x: Union[int, float] = 0) -> "Polygon":
        """Reflects all vertices of the polygon across a vertical line."""
        reflected_points = [p.reflect_y(axis_x) for p in self._points]
        return Polygon(reflected_points)

    def reflect_origin(self) -> "Polygon":
        """Reflects all vertices of the polygon about the origin."""
        reflected_points = [p.reflect_origin() for p in self._points]
        return Polygon(reflected_points)

    def reflect_xy_line(self) -> "Polygon":
        """Reflects all vertices of the polygon across the line y = x."""
        reflected_points = [p.reflect_xy_line() for p in self._points]
        return Polygon(reflected_points)
