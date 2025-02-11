#1
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

#пример использования
N = 10
for square in square_generator(N):
    print(square)


#2
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

#ввод в консоль
n = int(input("Enter a number: "))
print(",".join(map(str, even_generator(n))))


#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

#пример
n = 50
for num in divisible_by_3_and_4(n):
    print(num)


#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

#пример
a, b = 3, 8
for val in squares(a, b):
    print(val)


#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

#=пример
n = 5
for num in countdown(n):
    print(num)
