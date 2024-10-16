# 12)Create a Python function calculate_area(radius) that calculates the area of a circle given its radius. Use math.pi for π.

def calculate_area(radius):
    area= 3.142*radius*radius
    return area
x=int(input("enter radius of ciircle "))

calculate_area(x)

area = calculate_area(x)
