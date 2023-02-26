from vector import Vector
import random

class Point:
    """
    A point class that has a x and y coordinate and a vector
    @param x: the x coordinate of the point
    @param y: the y coordinate of the point
    @param vector: the vector of the point
    """
    def __init__(self, x_coordinate, y_coordinate, vector_function=lambda: Vector(2*random.random()-1, 2*random.random()-1) ):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.vector_function = vector_function

    @classmethod
    def random_point(cls, system_width: int, system_height: int) -> 'Point':
        """
        returns a random point within the system
        @param system_width: the width of the system
        @param system_height: the height of the system
        @return: a random point within the system
        """
        return Point(random.randint(-system_width//2, system_width//2), random.randint(-system_height//2, system_height//2))

    @classmethod
    def position_after_vector(cls, point, vector: Vector) -> 'Point':
        """
        returns the position of a point after a vector has been applied
        @param point: the point to apply the vector to
        @param vector: the vector to apply to the point
        @return: the position of the point after the vector has been applied
        """
        return Point(point.get_x() + vector.get_x_velocity(), point.get_y() + vector.get_y_velocity(), point.get_vector_function())

    def get_x(self) -> int:
        """returns the x coordinate of the point"""
        return self.x_coordinate

    def get_y(self) -> int:
        """returns the y coordinate of the point"""
        return self.y_coordinate

    def get_xy(self) -> tuple:
        """returns the x and y coordinate of the point"""
        return self.x_coordinate, self.y_coordinate

    def set_X(self, new_x_coordinate: int):
        """
        updates the x coordinate of the point
        @param x: the x coordinate to update to
        """
        self.x_coordinate = new_x_coordinate

    def set_y(self, new_y_coordinate: int):
        """
        updates the y coordinate of the point
        @param y: the y coordinate to update to
        """
        self.y_coordinate = new_y_coordinate

    def set_xy(self, new_point):
        """
        updates the x and y coordinate of the point
        @param x: the x coordinate to update to
        @param y: the y coordinate to update to
        """
        self.x_coordinate, self.y_coordinate = new_point.get_xy()

    def get_vector_function(self):
        return self.vector_function
    
    def intersects(self, point, radius1, radius2) -> bool:
        """
        returns if the point is within the radius of another point
        @param point: the point to check if it is within the radius of
        @param radius1: the radius of the coorosponding particle for this point
        @param radius2: the radius of the coorosponding particle for the point to check
        """
        
        """
        sums the radii of the two circles so it only checks if the center of the circle is 
        within the radius of circle with the sum of the radii, and by extension if the original
        circles are intersecting
        """
        return abs(self.get_x() - point.get_x()) <= radius1+radius2 and abs(self.get_y() - point.get_y()) <= radius1+radius2
