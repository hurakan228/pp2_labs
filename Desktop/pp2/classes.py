



#ClassesString
class StringManipulator:
    def getString(self):
        self.input_string = input("Enter a string: ")
    
    def printString(self):
        print(self.input_string.upper())


#ShapeArea
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# Пример использования
square = Square(4)
print("Area of the square:", square.area())


#Class Rectangle 
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#пример
rectangle = Rectangle(5, 3)
print("Area of the rectangle:", rectangle.area())


#class Point
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

#Пример
point1 = Point(0, 0)
point2 = Point(3, 4)
point1.show()
point1.move(2, 3)
point1.show()
print("Distance between point1 and point2:", point1.dist(point2))



#Bank 
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

#Пример
account = Account("John", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)




#lambda, filter
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#List
numbers = [10, 11, 13, 16, 17, 18, 19, 20, 23, 25]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)
