# main.py
from functions import grams_to_ounces, fahrenheit_to_celsius, solve, filter_prime, reverse_words, has_33, spy_game

def main():
    print("Convert 100 grams to ounces:", grams_to_ounces(100))
    print("Convert 100°F to Celsius:", fahrenheit_to_celsius(100))
    print("Solve for 35 heads and 94 legs:", solve(35, 94))
    print("Filter prime numbers from [10, 15, 17, 19, 21]:", filter_prime([10, 15, 17, 19, 21]))
    print("Reverse words in 'We are ready':", reverse_words("We are ready"))
    print("Check if [1, 3, 3] contains 33:", has_33([1, 3, 3]))
    print("Check if [1,2,4,0,0,7,5] contains 007 in order:", spy_game([1,2,4,0,0,7,5]))

if __name__ == "__main__":
    main()
