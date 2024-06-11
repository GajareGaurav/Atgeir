import math

def distance_3d(x1, y1, z1, x2, y2, z2):

    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    return math.sqrt(dx**2 + dy**2 + dz**2)

# LETS TAKE RANDOM 6 DISTANCE
point1 = (99,69 ,35 )
point2 = (999, 69, 23)

x1, y1, z1 = point1
x2, y2, z2 = point2

distance = distance_3d(x1, y1, z1, x2, y2, z2)
print(f"The distance between {point1} and {point2} is {distance:.2f}")
