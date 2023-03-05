import numpy as np
import pandas as pd
from vector import Vector
from point import Point

class Particle:
    """
    A class to represent a particle in 2d space
    @param coordinate: the coordinate of the particle of class point
    @param radius: the radius of the particle
    @param color: the color of the particle
    """
    def __init__(self, coordinate=Point([0,0]), radius=1, color='b'):
        self.coordinate = coordinate
        self.radius = radius
        self.color = color
        
    @classmethod
    def copy(cls, particle: 'Particle') -> 'Particle':
        """
        creates and returns a copy of the given particle
        @param particle: the particle to copy
        """
        copy_particle = cls(particle.get_point(), particle.get_radius(), particle.get_color())
        return copy_particle
        
    def get_point(self) -> Point:
        """returns the point object of the particle"""
        return self.coordinate
    
    def set_xy(self, new_x: int, new_y: int):
        """
        sets the x and y coordinates of the particle
        @param new_x: the new x coordinate of the particle
        @param new_y: the new y coordinate of the particle
        """
        self.get_point().set_x(new_x)
        self.get_point().set_y(new_y)
        
    def set_x(self, new_x: int):
        """
        sets the x coordinate of the particle
        @param new_x: the new x coordinate of the particle
        """
        self.get_point().set_x(new_x)
        
    def set_y(self, new_y: int):
        """
        sets the y coordinate of the particle
        @param new_y: the new y coordinate of the particle
        """
        self.get_point().set_y(new_y)
        
    def get_x(self) -> int:
        """returns the x coordinate of the particle"""
        return self.get_point().get_x()
    
    def get_y(self) -> int:
        """returns the y coordinate of the particle"""
        return self.get_point().get_y()
        
    def get_coordinates(self) -> np.ndarray:
        """returns the coordinates of the particle"""
        return self.get_point().get_coordinates()
    
    def get_radius(self) -> int:
        """returns the radius of the particle"""
        return self.radius
    
    def get_color(self) -> int:
        """returns the color of the particle"""
        return self.color
    
    def apply_vector(self, vector: Vector):
        """
        apply a vector to the particle
        @param vector: the vector to apply to the particle
        """
        self.coordinate.apply_vector(vector)
