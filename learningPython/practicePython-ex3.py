# BSD 3-Clause License

# Copyright (c) 2017, Darren Shelton
# All rights reserved.


def main():

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for x in a[:]:
        if x < 5:
            b.append(x)
    print(b)

if __name__ == '__main__':
    main()
