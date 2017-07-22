# BSD 3-Clause License

# Copyright (c) 2017, Darren Shelton
# All rights reserved.


def main():

    print("Provide a number and I will tell you its divisors")
    number = int(input("what is your number? "))
    check = range(2, number+1)

    print("The divisors are: ")
    for i in check:
        result = number % i
        if result == 0:
            print(i)

if __name__ == '__main__':
    main()
