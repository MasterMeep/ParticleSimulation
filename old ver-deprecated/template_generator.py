from point import Point
from vector import Vector
from system import System
from alive_progress import alive_bar
from particle import Particle
import math


def generate_square(side_length, particle, system):
    for y in range(-side_length//2, side_length//2):
        for x in range(-side_length//2, side_length//2):
            particle = Particle.copy_particle(particle)
            particle.set_xy(Point(x, y))
            system.add_particle(particle)
                
def generate_nested_squares(side_length_inner, side_length_outer, particle_inner, particle_outer, system, density=1):
    for y in range(-(side_length_inner+side_length_outer)//2, (side_length_inner+side_length_outer)//2, density):
        for x in range(-(side_length_inner+side_length_outer)//2, (side_length_inner+side_length_outer)//2, density):
            if 0 <= x:
                particle = Particle.copy_particle(particle_inner)
            else:
                particle = Particle.copy_particle(particle_outer)
            particle.set_xy(Point(x, y))
            system.add_particle(particle)

def generate_particle_density(particle, density, system):
    system_area = system.get_width()*system.get_height()
    particle_area = math.pi*(particle.get_radius()**2)
    particle_amount = int((system_area*density)/particle_area)
    system.add_multiple_duplicate_particles(particle, particle_amount)