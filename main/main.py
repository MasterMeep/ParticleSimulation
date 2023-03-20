from particle import Particle
from vector import Vector
from point import Point
from system import System
import time
import random
from template_generator import generate_square, generate_nested_squares, generate_particle_density

import warnings
warnings.filterwarnings("ignore")


vector_randomization = lambda: Vector(6*random.random()-3, 6*random.random()-3)
test_particle1 = Particle(vector_function = vector_randomization, radius = 1)
test_particle2 = Particle(vector_function = vector_randomization, radius = 2, color='r')





test_system = System(width = 100, height = 100, gravity = False, step_size = 1000)

generate_particle_density(test_particle1, 0.4, test_system)
#generate_particle_density(test_particle2, 0.2, test_system)

print(len(test_system.get_particles()))
#test_system.add_multiple_duplicate_particles(test_particle1, 3)
test_system.step(steps=10, show=True)
#test_system.show_state()
test_system.animate_plots(show_density=True, show_step_states=True, show_individually=True)