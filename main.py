from particle import Particle
from vector import Vector
from point import Point
from system import System
import time
import random


vector_randomization = lambda: Vector(2*random.random()-1, 2*random.random()-1) 
test_particle = Particle(x_coordinate = 0, y_coordinate = 0, vector = vector_randomization, radius = 1)




test_system = System(width = 100, height = 100, gravity = False, step_size = 10)

test_system.add_multiple_duplicate_particles(test_particle, 5)
test_system.animate_plots()