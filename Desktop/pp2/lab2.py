#Booleans 
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("hello"))
print(bool(15))

x = 'Hello'
y = 15
print(bool(x))
print(bool(y))

#Operators 
print(10+5)

print((5-1)+(4-1))

print(40+4*3)

print(5+2+4-10)

#Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits = ["apple", "banana", "cherry", "apple", "cherry"]
print(fruits)


print(len(fruits))

numbers = [1, 5, 7, 9, 3]
booleans = [True, False, False]
mixed = ["abc", 34, True, 40, "male"]

print(fruits)
print(numbers)
print(booleans)
print(mixed)


print(type(fruits))


new_list = list(("apple", "banana", "cherry"))
print(new_list)


print(fruits[1])  
print(fruits[-1])  


long_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(long_list[2:5])
print(long_list[:4])  
print(long_list[2:])  

#Tuples 
mytuple = ("pear", "orange", "grape")
print(mytuple)

mytuple = ("pear", "orange", "grape")
print(len(mytuple))

single_tuple = ("pear",)
print(type(single_tuple))

not_a_tuple = ("pear")
print(type(not_a_tuple))

tuple1 = ("pear", "orange", "grape")
tuple1 = (2,8,12,7,9)
tuple3 = (True, False, True)

mixed_tuple = ("xyz", 25, False, 36, "female")
print(type(mixed_tuple))

mytuple = tuple(("pear", "orange", "grape"))
print(mytuple)


#Set
myset = {"pear", "orange", "grape"}
print(myset)

myset = {"pear", "orange", "grape"}
print(len(myset))

set1 = {"pear", "orange", "grape"}
set2 = {2,8,12,7,9}
set3 = {True, False, False}

myset = set(("pear", "orange", "grape"))
print(myset)


#Dictionaries
mydict = {
  "brand": "BMW",
  "model": "M5 F90",
  "year": 2020
}
print(mydict)

mydict = {
  "brand": "BMW",
  "model": "M5 F90",
  "year": "2020"
}
print(mydict["brand"])
print(len(mydict))

mydict = dict(name = "Muhammed", age = 19, country = "KZ")
print(mydict)


#If-else
a = 50
b = 100
if b > a:
  print("b больше чем а")

  a = 50
  b = 50 
  if b > a:
    print("b больше чем а")
elif a == b:
  print("a и b равны")

a = 100
b = 50
if b > a:
    print("b больше, чем a")
elif a == b:
    print("a и b равны")
else:
    print("a больше, чем b")


a = 200
b = 300
print("A") if a > b else print("=") if a == b else print("B")


a = 100
b = 50
c = 200
if a > b and c > a:
    print("Оба условия истинны")


a = 100
b = 50
c = 200
if a > b or a > c:
    print("Хотя бы одно условие истинно")


a = 50
b = 100
if not a > b:
    print("a не больше, чем b")


x = 15
if x > 10:
    print("Больше 10,")
    if x > 20:
        print("и больше 20!")
    else:
        print("но не больше 20.")


a = 50
b = 100
if b > a:
    pass 


#While loops 
#Basic while
i = 1
while i < 6:
    print(i)
    i += 1


i = 1
while i < 6:
    print(i)
    if i == 3:
        break  
    i += 1


i = 0
while i < 6:
    i += 1
    if i == 3:
        continue 
    print(i)


i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i больше или равен 6, цикл завершен")


i = 0
while i < 10:
    print(i)
    i += 2  



#For Loops
fruits = ["pear", "orange", "grape"]
for x in fruits:
    print(x)


fruits = ["pear", "orange", "grape"]
for x in fruits:
    print(x)
    if x == "orange":
        break 


fruits = ["pear", "orange", "grape"]
for x in fruits:
    if x == "orange":
        continue 
    print(x)


for x in range(5):
    print(x)


for x in range(5):
    if x == 2:
        break  
    print(x)
else:
    print("Цикл завершен!")


adj = ["small", "sweet", "fresh"]
fruits = ["pear", "orange", "grape"]

for x in adj:
    for y in fruits:
        print(x, y)
