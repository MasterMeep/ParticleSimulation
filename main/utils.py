import math

def circles_intersect(x1, y1, r1, x2, y2, r2):
	distance_between_centers = math.sqrt((x1-x2)**2+(y1-y2)**2)
	sum_of_radii_squared = (r1+r2)**2

	value = distance_between_centers < sum_of_radii_squared

	return value