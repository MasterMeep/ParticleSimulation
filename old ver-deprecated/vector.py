class Vector:
    """
    Vector class that has a x and y velocity
    @param x_velocity: the x velocity of the vector
    @param y_velocity: the y velocity of the vector
    """    
    def __init__(self, x_velocity=0, y_velocity=0):
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def get_x_velocity(self) -> int:
        """returns the x velocity of the vector"""
        return self.x_velocity

    def get_y_velocity(self) -> int:
        """returns the y velocity of the vector"""
        return self.y_velocity

    def set_vector(self, new_x_velocity: int, new_y_velocity: int, new_z_velocity: int):
        """
        updates the vector
        @param x_velocity: the x velocity to update to
        @param y_velocity: the y velocity to update to
        """
        self.x_velocity = new_x_velocity
        self.y_velocity = new_y_velocity
        self.z_velocity = new_z_velocity