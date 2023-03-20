import numpy as np
from random import uniform, randint
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from math import ceil, sqrt

from Particle import Particle
from utils import circles_intersect
from Grid import Grid

class System:
    def __init__(self, side_length):
        self.side_length = side_length
        self.unordered_particles = []
        self.max_radii = 4
        self.segmented_particle_grid_size = side_length//self.max_radii
        self.reset_segmented_particle_grid()
        self.index = 0

    def add_n_points(self, particle, amount):
        for i in range(amount):
            self.unordered_particles.append(Particle.copy(particle))
            
    def setup_particle_lattice(self):
        for i, particle in enumerate(self.unordered_particles):
            amount = len(self.unordered_particles)
            particle.x = (i % ceil(sqrt(amount))) * self.side_length / ceil(sqrt(amount))
            particle.y = (i // ceil(sqrt(amount))) * self.side_length / ceil(sqrt(amount))
        
    def add_particle(self, particle):
        self.unordered_particles.append(particle)

    def show(self, show=True):
        for point in self.unordered_particles:
            circle = plt.Circle((point.x, point.y), point.radius, color=point.color, fill=False)
            plt.gca().add_patch(circle)

        plt.axis('scaled')
        if show:    
            plt.show()

    def animate(self, step_size, step_amount_per_frame):
        fig, ax = plt.subplots()
        def animation(frame):
            for i in range(step_amount_per_frame):
                self.segmented_step(step_size)
            ax.clear()
            self.show(show=False)
            plt.title(self.index)
            self.index += step_amount_per_frame
        animation_variable = FuncAnimation(fig, animation, frames=100)
        plt.show()

    def naive_check(self, point):
        for iteratedPoint in self.unordered_particles:
            if iteratedPoint != point:
                if circles_intersect(*iteratedPoint.get_xyr(), *point.get_xyr()):
                    return False

        return True
    
    def naive_benchmark(self):
        for particle in self.unordered_particles:
            self.naive_check(particle)
        
    def reset_segmented_particle_grid(self):
        self.segmented_particle_grid = np.zeros((self.segmented_particle_grid_size, self.segmented_particle_grid_size), object)
        for x in range(self.segmented_particle_grid_size):
            for y in range(self.segmented_particle_grid_size):
                self.segmented_particle_grid[y, x] = Grid()
                
    def get_segmented_coordinate(self, particle):
        return int(particle.x//self.max_radii), int(particle.y//self.max_radii)
    
    def add_particle_to_segmented_particle_grid(self, particle):
        x, y = self.get_segmented_coordinate(particle)
        self.segmented_particle_grid[y, x].add_particle(particle)
        
    def get_particles_from_segmented_particle_grid(self, x, y):
        segmented_x, segmented_y = self.get_segmented_coordinate(Particle(x=x, y=y))
        return self.segmented_particle_grid[segmented_y, segmented_x].particles
    
    def get_grid_slice_from_segmented_grid(self, center, width):
        x,y = center
        particles = []
        for x_slice in range(max(x-self.max_radii, 0), min(x+self.max_radii+1, self.side_length), self.max_radii):
            for y_slice in range(max(y-self.max_radii, 0), min(y+self.max_radii+1, self.side_length), self.max_radii):
                particles.extend(self.get_particles_from_segmented_particle_grid(x_slice, y_slice))
                
        return particles
    
    def segmented_check_particle(self, particle, slice_width=1):
        for iteratedParticle in self.get_grid_slice_from_segmented_grid((int(particle.x), int(particle.y)), slice_width):
            if iteratedParticle != 0 and iteratedParticle != particle:
                if circles_intersect(*particle.get_xyr(), *iteratedParticle.get_xyr()):
                    return False
        return True
    
    def load_all_particles_to_segmented_grid(self):
        for particle in self.unordered_particles:
            self.add_particle_to_segmented_particle_grid(particle)
            
    def update_particle_position_in_segmented_grid(self, particle, original_x, original_y):
        x, y = self.get_segmented_coordinate(Particle(x=original_x, y=original_y))
        self.segmented_particle_grid[y, x].remove(particle)
        self.add_particle_to_segmented_particle_grid(particle)
    
    def segmented_benchmark(self):
        self.reset_segmented_particle_grid()
        for particle in self.unordered_particles:
            if not self.segmented_check_particle(particle):
                print('failed')
            self.add_particle_to_segmented_particle_grid(particle)
                
                
    def naive_randomize(self):
        for particle in self.unordered_particles:
            running = True
            index = 0
            while running:
                particle.x = uniform(0, self.side_length)
                particle.y = uniform(0, self.side_length)
                if self.naive_check(particle) or index > 100:
                    running = False
                    
                index += 1
                    
    def segmented_randomize(self):
        self.reset_segmented_particle_grid()
        for particle in self.unordered_particles:
            running = True
            index = 0
            while running:
                particle.x = uniform(0, self.side_length)
                particle.y = uniform(0, self.side_length)
                if self.segmented_check_particle(particle) or index > 100:
                    self.add_particle_to_segmented_particle_grid(particle)
                    running = False
                    
                index += 1

    def segmented_step(self, step_width):
        for particle in self.unordered_particles:
            original_x = particle.x
            original_y = particle.y
            particle.x += uniform(-step_width, step_width)
            particle.y += uniform(-step_width, step_width)
            particle.x = max(1, min(particle.x, self.side_length-1))
            if not self.segmented_check_particle(particle) or particle.x < 0.0 or particle.x > self.side_length or particle.y < 0.0 or particle.y > self.side_length:
                particle.x = original_x
                particle.y = original_y

            self.update_particle_position_in_segmented_grid(particle, original_x, original_y)