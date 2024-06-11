import math

def cal_circle_area(radius):
    
    area = math.pi * math.pow(radius, 2)
    return area

radius = float(input("Enter the radius of the circle: "))

area = cal_circle_area(radius)


print("The area of the circle is:", area)
