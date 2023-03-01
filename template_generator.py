from point import Point
from vector import Vector
from system import System
from alive_progress import alive_bar
from particle import Particle

def generate_square(side_length, particle, system):
    with alive_bar(side_length**2, title='Generating Square') as bar:
        for y in range(-side_length//2, side_length//2):
            for x in range(-side_length//2, side_length//2):
                particle = Particle.copy_particle(particle)
                particle.set_xy(Point(x, y))
                system.add_particle(particle)
                bar()
                
def generate_nested_squares(side_length_inner, side_length_outer, particle_inner, particle_outer, system):
    with alive_bar((side_length_inner+side_length_outer)**2, title='Generating Square') as bar:
        for y in range(-(side_length_inner+side_length_outer)//2, (side_length_inner+side_length_outer)//2):
            for x in range(-(side_length_inner+side_length_outer)//2, (side_length_inner+side_length_outer)//2):
                if -side_length_inner//2 <= x <= side_length_inner//2 and -side_length_inner//2 <= y <= side_length_inner//2:
                    particle = Particle.copy_particle(particle_inner)
                else:
                    particle = Particle.copy_particle(particle_outer)
                particle.set_xy(Point(x, y))
                system.add_particle(particle)
                bar()