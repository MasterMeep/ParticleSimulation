from vector import Vector
from point import Point
from particle import Particle
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from alive_progress import alive_bar
import math
import seaborn as sns
from contextlib import nullcontext


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
        self.current_step = 0
        
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
            self.add_particle(Particle.copy_particle(particle))
        with alive_bar(amount, dual_line=True, title='Initializing Particles') as bar:
            for iterated_particle in self.get_particles():
                running = True
                while running:    
                    random_point = Point.random_point(self.width, self.height)
                    for second_iterated_particle in self.get_particles():
                        if not random_point.intersects(particle.get_coordinate(), iterated_particle.get_radius(), second_iterated_particle.get_radius()):
                            iterated_particle.get_coordinate().set_xy(random_point)
                            running = False
                            break
                
                bar()
        print(' ')
                

    def step(self, steps=1, show=False):
        """
        Steps the system by the amount of steps given
        @param steps: the amount of steps to step the system by
        """
        with alive_bar(steps, dual_line=True, title='Stepping') if show else nullcontext() as bar :
        
            for step in range(steps):
                for particle in self.particles:
                    particle.step(self.width, self.height, self)
                if(show):
                    bar()

        self.current_step += steps

    def show_state(self, axs=None, plot=True, show_density=False, animation=False):
        """display state of system with matplotlib"""
        
        if not animation:
            fig, axs = plt.subplots()
        
        x_coordinates = []
        y_coordinates = []
        sizes = []
        colors = []
        
        x_coordinates.clear()
        y_coordinates.clear()
        sizes.clear()
        colors.clear()
        for particle in self.particles:
            x_coordinates.append(particle.get_x())
            y_coordinates.append(particle.get_y())
            sizes.append(math.pi*(particle.get_radius()**2))
            colors.append(particle.get_color())
        if show_density:
            axs[0].set_title(self.current_step)
            axs[0].clear()
            axs[1].clear()
            axs[0].scatter(x_coordinates, y_coordinates, s=sizes, c=colors)
            
            axs[0].set_xlim([-self.width//2, self.width//2])
            axs[1].set_xlim([-self.width//2, self.width//2])
            
            axs[0].set_ylim([-self.height//2, self.height//2])
            axs[1].set_ylim([-self.height//2, self.height//2])
            
            
            sns.kdeplot(x_coordinates, y_coordinates, ax=axs[1], shade_lowest=False, cmap="Blues")
        else:
            axs.set_title(self.current_step)
            axs.clear()
            axs.scatter(x_coordinates, y_coordinates, s=sizes, c=colors)
            axs.set_xlim([-self.width//2, self.width//2])
            axs.set_ylim([-self.height//2, self.height//2])
            
        if plot:
            plt.show()
        

        
    def animate_plots(self, show_density=False):
        if show_density:
            fig, axs = plt.subplots(2,1)
        else:
            fig, axs = plt.subplots()
        
        def animate_system(frame):
            self.step(self.step_size)
            
            self.show_state(axs, plot = False, show_density=show_density, animation=True)
            if show_density:
                axs[0].set_title("Step: " + str(self.current_step))
            else:
                axs.set_title("Step: " + str(self.current_step))
        animation = FuncAnimation(fig, animate_system, interval=100)
        plt.show()


    def get_particle_coordinate_list(self) -> list:
        """
        Returns a list of the coordinates of all the particles in the system
        @return: a list of the coordinates of all the particles in the system
        """
        coordinates = []
        for particle in self.particles:
            coordinates.append(particle.get_coordinate())
            
        return coordinates
    
    def get_particle_coordinates_in_2d_list(self) -> list:
        particle_coordinates_2d = []
        for particle in self.get_particles():
            particle_coordinates_2d.append([*particle.get_coordinate().get_xy()])
            
        return particle_coordinates_2d
        
    def get_particles(self):
        return self.particles
    
    def get_width(self) -> int:
        """return the width of system"""
        return self.width