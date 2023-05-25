def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    if number % 3 != 0 and number % 5 == 0:
        print("Buzz")
