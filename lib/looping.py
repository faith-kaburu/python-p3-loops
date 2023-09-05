#!/usr/bin/env python3

def happy_new_year():
    count = 10
    
    while count >= 1:
        print(count)
        count -= 1
    
    print("Happy New Year!")

happy_new_year()

def square_integers(num_list):
    squared_nums = [num ** 2 for num in num_list]
    return squared_nums

input_list = [1, 2, 3, 4, 5]
squared_list = square_integers(input_list)
print(squared_list)

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Call the fizzbuzz function
fizzbuzz()