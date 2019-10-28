#!/usr/bin/env python3

# Created by: Austin-Harty
# Created on: October 2019
#  This program calculates to the power of user input


def main():
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            print()

            for loop_counter in range(number + 1):
                calculation = loop_counter ** 2
                print(str(loop_counter) + "^2", "=", str(calculation))

            if number < 0:
                print("Invalid, enter a positive integer.")
                print()
                continue

        except ValueError:
            print()
            print("Invalid Input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
