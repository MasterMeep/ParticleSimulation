class Grid:
    def __init__(self):
        self.particles = []
        
    def __repr__(self):
        return(str(self.particles))    
        
    def add_particle(self, particle):
        self.particles.append(particle)
        
    def remove(self, particle):
        self.particles.remove(particle)