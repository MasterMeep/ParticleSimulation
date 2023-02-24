from classes import Point, Vector

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
    def __init__(self, x_coordinate: int, y_coordinate: int, vector=Vector(0,0), mass=1, charge=0, gravity_effected=False):
        self.coordinate = Point(x_coordinate, y_coordinate, vector)
        self.vector = vector
        self.mass = mass
        self.charge = charge
        self.gravity_effected = gravity_effected

    def __repr__(self):
        return f'Particle\n\tPos: {self.get_x(), self.get_y()}'

    def get_new_pos(self):
        """returns the new position of the particle"""
        return self.vector.get_new_x(self.get_x()), self.vector.get_new_y(self.get_y())

    def update_pos(self):
        """
        updates the position of the particle to the new position of the
        particle after the vector has been stepped
        """
        new_pos = self.get_new_pos()
        self.coordinate = Point(new_pos[0], new_pos[1], self.vector)

    def get_x(self):
        """returns the x coordinate of the particle"""
        return self.coordinate.get_x()

    def get_y(self):
        """returns the y coordinate of the particle"""
        return self.coordinate.get_y()
