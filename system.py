from vector import Vector
from point import Point
from particle import Particle
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from alive_progress import alive_bar
import math



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
            
        self.current_step += steps

    def show_state(self, ax=None, plot=True):
        """display state of system with matplotlib"""
        if ax == None:
            fig, ax = plt.subplots()
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
        ax.set_title(self.current_step)
        ax.clear()
        ax.scatter(x_coordinates, y_coordinates, s=sizes, c=colors)
        ax.set_xlim([-self.width//2, self.width//2])
        ax.set_ylim([-self.height//2, self.height//2])
        
        if plot:
            plt.show()
        

        
    def animate_plots(self):
        fig, ax = plt.subplots()
        
        def animate_system(frame):
            self.step(self.step_size)
            
            self.show_state(ax, plot = False)
            ax.set_title("Step: " + str(self.current_step))
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
    
    def get_particles(self):
        return self.particles
    
    def get_width(self) -> int:
        """return the width of system"""
        return self.width