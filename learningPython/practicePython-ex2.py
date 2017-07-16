#
# BSD 3-Clause License

# Copyright (c) 2017, Darren Shelton
# All rights reserved.
#

# I started teaching myself python utilizing the exercises on http://www.practicepython.org/exercises.
# This is my solution to Exercise 2.


def main():

    print("Provide a number and I will tell you if it is odd or even")
    number = int(input("what is your number? "))
    check = int(input("What number would you like to check with? "))
    result = int(number) % 2
    result2 = int(number) % 4

    if int(result2) == 0:
        print("The number you provided, " + str(number) + " is divisible by 4.\n")
    elif int(result) == 0:
        print("The number you provided, " + str(number) + " is even.\n")
    else:
        print("The number you provided, " + str(number) + " is odd.\n")

    if number % check == 0:
        print(str(number) + " divides evenly by " + str(check))
    else:
        print(str(number) + " does not divide evenly by " + str(check))


if __name__ == '__main__':
    main()
