def leap_year():
    """
    Checks if a year is a leap-year or not
    :return: None
    """

    year = int(input("What year are you checking?: "))

    if year % 4 == 0 and year % 100 != 0:
        print("It is a leap-year!")
    elif year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
        print("It is a leap-year!")
    else:
        print("It is not a leap-year :(")