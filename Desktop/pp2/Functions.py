#Functions
def grams_to_ounces(grams):
    return 28.3495231 * grams

def farenheit_to_celsius(farenheit):
    return(5 / 9) * (farenheit - 32)

def solve(numheads, numlegs):
    for chicken in range(numheads + 1):
        rabbits = numheads - chickens 
        if(chickens * 2 + rabbits * 4) == numlegs:
            return chickens,rabbits
        return None
    
def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n))+ 1):
            if n % i == 0:
                return False
            return True
        return[num for num in numbers if is_prime(num)]

def string_permutations(s):
    return list(map("".join, itertools.permutations(s)))

def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

def has_33(nums):
    return any(nums[i] == nums[i+1] == 3 for i in range(len(nums)-1)) 

def spy_game(nums):
    pattern = [0,0,7]
    index = 0
    for num in nums:
        if num == pattern[index]:
            index += 1
            if index == len(pattern):
                return True
            return False

def sphere_volume(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item) 
            
    return unique_list


def is_palindrome(s):
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print("*"* num)


def guess_number():
    name = input("hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
        
    