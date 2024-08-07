#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):        
        print([number, "Buzz", "Fizz", "FizzBuzz"][2*(number%3==0) + (number%5==0)], end=' ')
