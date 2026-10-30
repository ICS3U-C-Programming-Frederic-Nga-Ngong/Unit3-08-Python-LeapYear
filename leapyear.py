#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 18 2008
# Tell the user if he can date my grandchild or not.


def main():
    # Get the year from the user
    year_str = input("Enter a year\n")

    # Cast it into an integer
    try:
        year_int = int(year_str)

        # Check if the year is divisible by 4 and 100 or by 4 and 400
        if year_int % 4 == 0:
            if year_int % 100 != 0:
                print("{} is a leap year".format(year_int))
            elif year_int % 400 == 0:
                print("{} is a leap year".format(year_int))
            else:
                print("{} is not a leap year".format(year_int))
        else:
            print("{} is not a leap year".format(year_int))

    # Tell the user the year he entered is not a valid one
    except ValueError:
        print("{} is not a valid year".format(year_str))


if __name__ == "__main__":

    main()
