def grade_converter():
    """
    Prints the letter equivalent of a given student's score
    :return: None
    """

    score = int(input("What's your score?: "))

    if 90 <= score <= 100:
        print("A")
    elif 80 <= score <= 89:
        print("B")
    elif 70 <= score <= 79:
        print("C")
    elif 60 <= score <= 69:
        print("D")
    else:
        print("F")