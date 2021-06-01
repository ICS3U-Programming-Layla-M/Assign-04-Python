#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May 28, 2021
# This program asks the user to enter a string,
# how many characters of the string, and how
# many times those characters should be repeated
# before displaying the subword

def main():
    global main_word
    # ask user to enter a string
    main_word = input("Enter a string: ")
    print("\n")
    subword_start()


def subword_start():
    global subword_start_int

    while True:
        # ask the user where the subword will start
        subword_start_string = input("At what index will the subword start? ")

        try:
            # check if input is an integer
            subword_start_int = int(subword_start_string)
            if (subword_start_int < 0):
                # check if size is negative
                print("{} is negative, try again.\
". format(subword_start_int))
            else:
                if (subword_start_int < len(main_word)):
                    # check if start is not bigger than word
                    print("\n")
                    subword_size()
                    break
                else:
                    # error message if start is not within bounds
                    print("{} does not have that many characters, try again.\
". format(main_word))
        except ValueError:
            # error message if not an integer
            print("{} is not a valid number, try again.\
 ". format(subword_start_string))


def subword_size():
    global char_number_int
    global main_word_sub

    while True:
        # ask user to enter the size of the subword
        char_number_string = input("Enter the size of the\
 subword: ")

        try:
            # check if size is an integer
            char_number_int = int(char_number_string)
            i = subword_start_int
            char_number_int_index = i + char_number_int
            main_word_sub = ""
            while (i < char_number_int_index):
                # create the subword
                c = main_word[i]
                main_word_sub += c
                i = i + 1
            if (char_number_int <= 0):
                # check if size is a not positive
                print("{} is not a positive number, try again.\
". format(char_number_int))
            else:
                print("\n")
                repetition()
                break
        except ValueError:
            # error message if not an integer
            print("{} is not a positive number, try again.\
". format(char_number_string))
        except IndexError:
            # error message if subword size is too big
            print("{} does not have that many characters, try again.\
". format(main_word_sub))


def repetition():
    global times_repeated_int

    while True:
        # ask user how many times to repeat subword
        times_repeated_string = input("How many times\
 should the subword repeat? ")
        try:
            # check if input is an integer
            times_repeated_int = int(times_repeated_string)
            if (times_repeated_int <= 0):
                # check if input is not positive
                print("{} is not a positive number, try\
 again.". format(times_repeated_int))
            else:
                output()
                break
        except ValueError:
            # error message if not an integer
            print("{} is not a positive number, try again.\
". format(times_repeated_string))


def output():
    # output the subword repeated number of times specified
    output_sub = main_word_sub*times_repeated_int
    print("\n")
    print("{}". format(output_sub))


if __name__ == "__main__":
    main()
