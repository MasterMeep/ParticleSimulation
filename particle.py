from point import Point
from vector import Vector

class Particle:
    """
    A particle class that has a coordinate, vector, mass, charge, and gravity effected
    @param x_coordinate: the x coordinate of the particle
    @param y_coordinate: the y coordinate of the particle
    @param vector: the vector of the particle
    @param mass: the mass of the particle
    @param charge: the charge of the particle
    @param gravity_effected: if the particle is effected by gravity
    """
    def __init__(self, x_coordinate: int, y_coordinate: int, vector_function, radius=1, charge=0, color='blue'):
        self.coordinate = Point(x_coordinate, y_coordinate, vector_function)
        self.radius = radius
        self.charge = charge
        self.color = color

    def __repr__(self):
        return f'Particle\n\tPos: {self.get_x(), self.get_y()}'

    
    @classmethod
    def copy_particle(cls, particle) -> 'Particle':
        """
        returns a copy of the particle
        @param particle: the particle to copy
        @return a copy of the particle
        """
        return cls(particle.get_x(), particle.get_y(), particle.get_vector_function(), particle.get_radius(), particle.get_charge(), particle.get_color())

    def get_new_pos(self, steps=0) -> Point:
        """returns the new position of the particle"""
        return self.coordinate.position_after_step(steps)

    def step(self, system_width: int, system_height: int, system, steps=1):
        """
        updates the position of the particle to the new position of the
        particle after the vector has been stepped
        @param system_width: the width of the system
        @param system_height: the height of the system
        @param steps: the amount of steps to step the vector by
        @param particle_coordinates: the coordinates of the other particles in the system
        """
        running = True
        while running:
            next_vector = self.get_vector_function()()
            next_position = self.get_coordinate().position_after_vector(self.get_coordinate(), next_vector)
            for particle in system.get_particles():
                if not next_position.intersects(particle.get_coordinate(), self.get_radius(), particle.get_radius()):
                    if -system_width//2 <= next_position.get_x() <= system_width//2 and -system_height//2 <= next_position.get_y() <= system_height//2:
                        self.get_coordinate().set_xy(next_position)
                        running = False
                        break

    def get_x(self) -> int:
        """returns the x coordinate of the particle"""
        return self.coordinate.get_x()

    def get_y(self) -> int:
        """returns the y coordinate of the particle"""
        return self.coordinate.get_y()
    
    def get_coordinate(self) -> Point:
        return self.coordinate

    def get_vector_function(self) -> Vector:
        """returns the vector of the particle"""
        return self.get_coordinate().get_vector_function()
    
    def get_radius(self) -> int:
        """returns the size of the particle"""
        return self.radius
    
    def get_charge(self) -> int:
        """returns the charge of the particle"""
        return self.charge
    
    def get_color(self) -> str:
        """returns the color of the particle"""
        return self.color