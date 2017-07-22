# BSD 3-Clause License

# Copyright (c) 2017, Darren Shelton
# All rights reserved.


def main():

    print("Provide a word, and I will check to see if it is a palindrome: \n")
    word = input("What is your word?")
    backwards_word = word[::-1]
    if str.lower(word) == str.lower(backwards_word):
        print("The word is a palindrome!")
    else:
        print("The word is not a palindrome, Try Again!")
if __name__ == '__main__':
    main()
