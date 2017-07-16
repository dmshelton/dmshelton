# BSD 3-Clause License

# Copyright (c) 2017, Darren Shelton
# All rights reserved.


def main():

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for x in a[:]:
        if x < 5:
            print(x)

if __name__ == '__main__':
    main()
