from particle import Particle
from point import Point
from vector import Vector
import numpy as np
from sklearn.neighbors import KDTree
from random import randint
from math import pi, sqrt
import pandas as pd
from matplotlib import pyplot as plt
from alive_progress import alive_bar
from matplotlib.animation import FuncAnimation


class System:
    """
    A system of particles
    @param side_length: the side length of the system
    @param step_size: the step size of the system
    @param gravity_enabled: whether or not gravity is enabled
    """
    def __init__(self, side_length, step_size, gravity_enabled=False):
        self.side_length = side_length
        self.step_size = step_size
        self.gravity_enabled = gravity_enabled
        self.unordered_particles = []
        self.particle_data = pd.DataFrame(columns=['x', 'y', 'radius', 'color'])
    
    def get_step_size(self) -> int:
        """Returns the step size of the system"""
        return self.step_size
    
    def get_side_length(self) -> int:
        """returns the side length of the system"""
        return self.side_length
    
    def get_particle_data(self) -> pd.DataFrame:
        """returns the particle data of the system"""
        return self.particle_data
    
    def append_particle_data(self, row: list):
        """
        appends a row to the particle data of the system
        @param row: the row to append to the particle data of the system, in the format [x, y, radius, color]
        """
        self.get_particle_data().append(row, ignore_index=True)
    
    def set_particle_data(self, particle_data: pd.DataFrame):
        """
        sets the particle data of the system to the new pandas dataframe
        @param particle_data: the new particle data of the system
        """
        self.particle_data = particle_data
        
    def get_particles(self) -> list:
        """returns a list of unordered particle objects in the system"""
        return self.unordered_particles
    
    def add_particle(self, particle: Point):
        """adds a particle to both the unordered particle list and the particle data dataframe of the system"""
        self.unordered_particles.append(particle)
        row_to_add = pd.DataFrame({'x': [particle.get_coordinates()[0][0]], 'y': [particle.get_coordinates()[0][1]],  'radius': [particle.get_radius()], 'color': [particle.get_color()]})
        self.set_particle_data(pd.concat([self.get_particle_data(), row_to_add], ignore_index=True, axis=0))
        
    def add_multiple_particles(self, particle: Particle, amount: int):
        used_coordinates = []
        with alive_bar(amount, dual_line=True, title='Initializing Particles') as bar:
            for _ in range(amount):
                generating_random_coordinates = True
                while generating_random_coordinates:
                    random_coordinate = (randint(0, self.side_length), randint(0, self.side_length))               
                    if random_coordinate not in used_coordinates:
                        copy_particle = Particle.copy(particle)
                        copy_particle.set_xy(*random_coordinate)
                        self.add_particle(copy_particle)
                        generating_random_coordinates = False
                    bar()
                    
                    
    
    def check_if_particle_is_valid(self, particle: Particle):
        x1,y1 = particle.get_coordinates()[0]
        r1 = particle.get_radius()
        system_side_length = self.get_side_length()
        
        def distance(x1,y1,x2,y2):
            return sqrt((x1-x2)**2 + (y1-y2)**2)
        
        for other_particle in self.get_particles():
            x2,y2 = other_particle.get_coordinates()[0]
            r2 = other_particle.get_radius()
            if distance(x1,y1,x2,y2) < r1 + r2 and 0 < x1 < system_side_length:
                return False
            
        return True
    
    def step(self, steps=1):
        new_particle_dataframe = pd.DataFrame(columns=['x', 'y', 'radius', 'color'])
        for particle in self.get_particles():
            generating_posibilities = True
            while generating_posibilities:
                
                random_vector = Vector.generate_random_vector(self.step_size)
                
                copied_particle = Particle.copy(particle)
                
                copied_particle.apply_vector(random_vector)
                
                if self.check_if_particle_is_valid(copied_particle):
                    particle.apply_vector(random_vector)
                    
                    # check if particle is out of bounds on the y axis
                    # and wraps it around if it is
                    
                    particle_y = particle.get_y()
                    
                    if particle_y < 0:
                        particle.set_y(self.get_side_length()+particle_y)
                    if particle.get_y() > self.get_side_length():
                        particle.set_y(particle_y-self.get_side_length())
                    particle_to_add = pd.DataFrame({'x': [particle.get_coordinates()[0][0]], 'y': [particle.get_coordinates()[0][1]],  'radius': [particle.get_radius()], 'color': [particle.get_color()]})
                    new_particle_dataframe = pd.concat([new_particle_dataframe, particle_to_add], ignore_index=True, axis=0)
                    generating_posibilities = False
        
        self.set_particle_data(new_particle_dataframe)
        
    def show(self):
        particle_data = self.get_particle_data()
        plt.scatter(particle_data['x'], particle_data['y'], c=particle_data['color'])
        plt.show()
        
    def animate(self):
        self.fig, self.ax = plt.subplots()
        def animation_function(frame):
            self.step(self.get_step_size())
            particle_data = self.get_particle_data()
            self.ax.scatter(particle_data['x'], particle_data['y'], c=particle_data['color'])
        animation = FuncAnimation(self.fig, animation_function, interval=100)
        plt.show()
