# BSD 3-Clause License

# Copyright (c) 2017, Darren Shelton
# All rights reserved.


def main():
    import random
    list_a = []
    list_b = []
    common_list = []
    for i in range(0, random.randint(0, 50)):
        list_a.append(random.randint(0, i))
    for j in range(0, random.randint(0, 50)):
        list_b.append(random.randint(0, j))
    print("Length of LIST_A: " + str(len(list_a)))
    print("Length of LIST_B: " + str(len(list_b)))
    print("LIST_A:" + str(list_a[:]))
    print("LIST_B:" + str(list_b[:]))
    for i in list_a[:]:
        if i in list_b:
            if int(i) not in common_list:
                common_list.append(i)
    print("Length of COMMON_LIST: " + str(len(common_list)))
    print("COMMON_LIST\n" + str(common_list[:]))
if __name__ == '__main__':
    main()
