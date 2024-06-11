import math

def cylinder_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    top_area = math.pi * radius**2
    total_area = lateral_area + 2 * top_area
    return total_area

def cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume


radius = float(input("radius of cylinder: "))
height = float(input("height of cylinder: "))

area = cylinder_area(radius, height)
volume = cylinder_volume(radius, height)


print(f"Area of cylinder: {area}")
print(f"Volume of cylinder: {volume}")
