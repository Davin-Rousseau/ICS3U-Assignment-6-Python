#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on: November 2019
# This program uses user defined functions
# To calculate surface area of a cube

import math


def surface_area_cube(l_c):
    # calculate surface area

    # process
    surface_area = (l_c ** 2) * 6

    # output
    return surface_area


def main():
    # This checks if input is an integer and positive,
    # then calls function and keeps going until user
    # enters a positive integer

    # Input
    input_1 = input("Enter the length of the cube(cm): ")
    print("")
    while True:
        try:
            length_cube = int(input_1)
            if length_cube > 0:
                # call functions
                surface_area = surface_area_cube(l_c=length_cube)
                print("The surface area of the cube is: {0:,.2f}cm^2"
                      .format(surface_area))
                break
            else:
                print("Invalid input")
                input_1 = input("Please try again: ")
                continue
        except ValueError:
            print("Invalid input.")
            input_1 = input("Please try again: ")
            continue


if __name__ == "__main__":
    main()
