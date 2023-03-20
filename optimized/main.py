from System import System
from Particle import Particle
import time

system = System(160)

test_particle = Particle()
system.add_n_points(test_particle, 1000)
system.setup_particle_lattice()
system.load_all_particles_to_segmented_grid()

print(len(system.unordered_particles))

system.show()

system.animate(10, 1000)

"""for i in range(50000):
    system.segmented_step(1)
    print(i)
system.show()"""

"""time1 = time.time()
system.naive_randomize()
print("Naive: " + str(time.time()-time1))"""


"""time1 = time.time()
system.segmented_randomize()
print("Segmented: " + str(time.time()-time1))

system.show()"""