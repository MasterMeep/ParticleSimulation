import numpy as np
from random import uniform

class Vector:
    """
    A vector
    @param x_component: the x component of the vector
    @param y_component: the y component of the vector
    @param z_component: the z component of the vector
    """
    def __init__(self, x_component: int, y_component: int):
        self.x_component = x_component
        self.y_component = y_component
        
    @classmethod
    def generate_random_vector(cls, step_size: int):
        vector = (uniform(-step_size, step_size), uniform(-step_size, step_size))
        return cls(*vector)
        
    def get_x_component(self) -> int:
        return self.x_component
    
    def get_y_component(self) -> int:
        return self.y_component
    
    def get_numpy_array(self):
        return np.array([[self.x_component], [self.y_component]])