from vector import Vector
from point import Point
from particle import Particle
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time



class System:
    """
    A collection of particles with functions that affect all particles in the system
    @param width: the width of the system
    @param height: the height of the system
    @param gravity: if the system is effected by gravity
    @param step_size: the amount of steps to step the system by during animation
    """
    def __init__(self, width, height, gravity=False, step_size=1):
        self.particles = []
        self.width = width
        self.height = height
        self.gravity = gravity
        self.step_size = step_size
        
    def add_particle(self, particle: Particle):
        """
        Adds a particle to the system
        @param particle: the particle to add to the system
        """
        self.particles.append(particle)
        
    def add_multiple_duplicate_particles(self, particle, amount):
        """
        Adds multiple particles to the system
        @param particle: the particle to add to the system
        @param amount: the amount of particles to add to the system
        """
        for _ in range(amount):
            self.particles.append(Particle.copy_particle(particle))
        for particle in self.get_particles():
            random_point = Point.random_point(self.width, self.height)
            particle.get_coordinate().set_xy(random_point)

    def step(self, steps=1):
        """
        Steps the system by the amount of steps given
        @param steps: the amount of steps to step the system by
        """
        for step in range(steps):
            for particle in self.particles:
                particle.step(self.width, self.height, self)
            """records steps. keep off unless debugging"""
            #if(step%10 == 0):
            #    print("Step: " + str(step) + " of " + str(steps) + " completed.")

    def show_state(self):
        """display state of system with matplotlib"""
        x = []
        y = []
        for particle in self.particles:
            x.append(particle.get_x())
            y.append(particle.get_y())
        plt.scatter(x, y)
        plt.xlim([-self.width//2, self.width//2])
        plt.ylim([-self.height//2, self.height//2])
        plt.show()
        

        
    def animate_plots(self):
        x_coordinates = []
        y_coordinates = []
        sizes = []
        
        fig, ax = plt.subplots()
        def animate_system(frame):
            self.step(self.step_size)
            x_coordinates.clear()
            y_coordinates.clear()
            sizes.clear()
            for particle in self.particles:
                x_coordinates.append(particle.get_x())
                y_coordinates.append(particle.get_y())
                sizes.append(particle.get_radius())
            ax.clear()
            ax.scatter(x_coordinates, y_coordinates, sizes)
            ax.set_xlim([-self.width//2, self.width//2])
            ax.set_ylim([-self.height//2, self.height//2])
            time.sleep(0.25)
        animation = FuncAnimation(fig, animate_system, interval=100)
        plt.show()

    """def animate_plots(self):
        x_coordinates = []
        y_coordinates = []
        fig, ax = plt.subplots()

        def animate_system(frame):
            self.step(self.step_size)
            x_coordinates.clear()
            y_coordinates.clear()
            for particle in self.particles:
                x_coordinates.append(particle.get_x())
                y_coordinates.append(particle.get_y())
            ax.clear()
            ax.scatter(x_coordinates, y_coordinates)
            ax.set_xlim([-self.width//2, self.width//2])
            ax.set_ylim([-self.height//2, self.height//2])
            time.sleep(0.25)
            
        animation = FuncAnimation(fig, animate_system, interval=100)
        
        plt.show()"""


    def get_particle_coordinate_list(self) -> list:
        """
        Returns a list of the coordinates of all the particles in the system
        @return: a list of the coordinates of all the particles in the system
        """
        coordinates = []
        for particle in self.particles:
            coordinates.append(particle.get_coordinate())
            
        return coordinates
    
    def get_particles(self):
        return self.particles