# BSD 3-Clause License

# Copyright (c) 2017, Darren Shelton
# All rights reserved.

# Trying to get this as one line
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = []
#for x in a[:]:
#    if x < 5:
#       b.append(x)
# print(b)

print([a for a in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if a < 5])

