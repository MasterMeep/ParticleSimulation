from particle import Particle
from vector import Vector
from point import Point
from system import System
import time
import random
import plotly.express as px 
import seaborn as sns
import pandas as pd

import warnings
warnings.filterwarnings("ignore")


vector_randomization = lambda: Vector(2*random.random()-1, 2*random.random()-1)
test_particle1 = Particle(x_coordinate = 0, y_coordinate = 0, vector_function = vector_randomization, radius = 1)
#test_particle2 = Particle(x_coordinate = 0, y_coordinate = 0, vector_function = vector_randomization, radius = 50, color='g')





test_system = System(width = 100, height = 100, gravity = False, step_size = 1)

test_system.add_multiple_duplicate_particles(test_particle1, 1000)

test_system.animate_plots(show_density=True)

#test_system.step(10000, show=True)