# BSD 3-Clause License

# Copyright (c) 2017, Darren Shelton
# All rights reserved.


def main():
    range_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    range_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    common_range = []
    for i in range_a[:]:
        if i in range_b:
            if int(i) not in common_range:
                common_range.append(i)
    print(common_range[:])
# if tarX in ('ini', 'txt') and act == 'm':
if __name__ == '__main__':
    main()
