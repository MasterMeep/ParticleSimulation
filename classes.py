class Vector:
    """
    Vector class that has a x and y velocity
    @param x_velocity: the x velocity of the vector
    @param y_velocity: the y velocity of the vector
    """
    def __init__(self, x_velocity, y_velocity):
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def get_x_velocity(self):
        """returns the x velocity of the vector"""
        return self.x_velocity

    def get_y_velocity(self):
        """returns the y velocity of the vector"""
        return self.y_velocity

    def update_vector(self, vector):
        """
        updates the vector
        @param vector: the vector to update to
        """
        self.x_velocity = vector.get_x_velocity()
        self.y_velocity = vector.get_y_velocity()

class Point:
    """
    A point class that has a x and y coordinate and a vector
    @param x: the x coordinate of the point
    @param y: the y coordinate of the point
    @param vector: the vector of the point
    """
    def __init__(self, x_coordinate, y_coordinate, vector = Vector(0,0)):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.vector = vector

    def step_vector(self, steps=1):
        """stepts the vector by the given amount of steps"""
        self.x_coordinate += self.vector.get_x_velocity()*steps
        self.y_coordinate += self.vector.get_y_velocity()*steps

    def get_x(self):
        """returns the x coordinate of the point"""
        return self.x_coordinate

    def get_y(self):
        """returns the y coordinate of the point"""
        return self.y_coordinate

    def get_xy(self):
        """returns the x and y coordinate of the point"""
        return self.x_coordinate, self.y_coordinate

    def update_X(self, x):
        """
        updates the x coordinate of the point
        @param x: the x coordinate to update to
        """
        self.x_coordinate = x

    def update_y(self, y):
        """
        updates the y coordinate of the point
        @param y: the y coordinate to update to
        """
        
        self.y_coordinate = y

    def update_xy(self, x, y):
        """
        updates the x and y coordinate of the point
        @param x: the x coordinate to update to
        @param y: the y coordinate to update to
        """
        self.x_coordinate, self.y_coordinate = x, y
