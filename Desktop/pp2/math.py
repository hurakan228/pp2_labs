#1
import math #type: ignore

def degree_to_radian(degree):
    return degree * (math.pi / 180)

#пример
degree = 15
print("Input degree:", degree)
print("Output radian:", round(degree_to_radian(degree), 6))



#2
def trapezoid_area(base1, base2, height):
    return ((base1 + base2) * height) / 2

#пример
height = 5
base1 = 5
base2 = 6
print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", trapezoid_area(base1, base2, height))



#3 
import math #type: ignore

def regular_polygon_area(num_sides, side_length):
    return (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))

#пример
num_sides = 4
side_length = 25
print("Input number of sides:", num_sides)
print("Input the length of a side:", side_length)
print("The area of the polygon is:", regular_polygon_area(num_sides, side_length))



#4
def parallelogram_area(base, height):
    return base * height

#пример
base = 5
height = 6
print("Length of base:", base)
print("Height of parallelogram:", height)
print("Expected Output:", parallelogram_area(base, height))

