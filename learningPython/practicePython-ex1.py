#
# BSD 3-Clause License

# Copyright (c) 2017, Darren Shelton
# All rights reserved.
#

# I started teaching myself python utilizing the exercises on http://www.practicepython.org/exercises.
# This is my solution to Exercise 1.


def main():

    from datetime import date
    thisyear = date.today().year

    print("Please provide your name and age you have turned in " + str(thisyear) + ".\n")
    name = input("name: ")
    age = input("age: ")

    print("Please enter another number. \n")
    secondnumber = input("number: ")

    year100 = thisyear + (100 - int(age))

    i = 0
    while i < int(secondnumber):
        if int(age) >= 100:
            print("Congrats, you are already 100 or older.\n")
            i = i + 1
        else:
            print("Hello " + name + ", you will be 100 years old in: " + str(year100) + "\n")
            i = i + 1


if __name__ == '__main__':
    main()
