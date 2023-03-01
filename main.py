from particle import Particle
from vector import Vector
from point import Point
from system import System
import time
import random
from template_generator import generate_square, generate_nested_squares

import warnings
warnings.filterwarnings("ignore")


vector_randomization = lambda: Vector(2*random.random()-1, 2*random.random()-1)
test_particle1 = Particle(x_coordinate = 0, y_coordinate = 0, vector_function = vector_randomization, radius = 1)
test_particle2 = Particle(x_coordinate = 0, y_coordinate = 0, vector_function = vector_randomization, radius = 1, color='g')





test_system = System(width = 100, height = 100, gravity = False, step_size = 1)

generate_nested_squares(50, 25, test_particle1, test_particle2, test_system)

#test_system.show_state()

test_system.animate_plots()

#test_system.step(10000, show=True)