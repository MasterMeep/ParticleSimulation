import numpy as np
from vector import Vector
from random import randint

class Point:
    """
    a class to represent a point in 2d space
    @param coordinates: the coordinates of the point in 3d space
    """
    def __init__(self, coordinate: list = []):
        self.coordinates = np.array([coordinate])
        
    @classmethod
    def generate_random_point(cls, system_side_length: int) -> 'Point':
        """
        generates a random point within the system size given
        @param system_side_length: the side length of the system size
        """
        return cls([randint(0, system_side_length), randint(0, system_side_length)])
        
        
    def apply_vector(self, vector: Vector):
        """
        applies a vector to the point
        @param vector: the vector to apply to the point
        """
        self.coordinates[0][0] += vector.get_x_component()
        self.coordinates[0][1] += vector.get_y_component()
        
    def get_coordinates(self) -> np.ndarray:
        """returns the list value of the coordinates of the point"""
        return self.coordinates
    
    def get_x(self) -> int:
        """returns the x coordinate of the point"""
        return self.coordinates[0][0]
    
    def set_x(self, new_x: int):
        """
        sets the x coordinate of the point
        @param new_x: the new x coordinate of the point
        """
        self.coordinates[0][0] = new_x
    
    def get_y(self) -> int:
        """returns the y coordinate of the point"""
        return self.coordinates[0][1]
    
    def set_y(self, new_y: int):
        """
        sets the y coordinate of the point
        @param new_y: the new y coordinate of the point
        """
        self.coordinates[0][1] = new_y