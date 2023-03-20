class Particle:
    def __init__(self,  x=0, y=0, radius=1, color='b'):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y

    """def __repr__(self):
        return("[" + str(self.x) + " " + str(self.y) + "]")"""

    @classmethod
    def copy(cls, point):
        return cls(radius=point.radius, x=point.x, y=point.y, color=point.color)
	
    def get_xyr(self):
        return self.x, self.y, self.radius
    