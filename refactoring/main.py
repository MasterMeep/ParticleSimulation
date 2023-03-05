from point import Point
from vector import Vector
from system import System
from particle import Particle

point = Point([1, 2])
system = System(100, 1, False)
particle = Particle(coordinate=point)

system.add_multiple_particles(particle, 5)

system.show()
system.step()
print(system.get_particles())
system.show()