# Luis Velasquez | module2_lab.py | Classify students based on their current grades

# Contains the students, sorted by their respective list
students = {}

while True:
    firstname = ""
    lastname = ""
    gpa = 0.0

    # Makes sure only letters are entered as a last name
    while True:
        lastname = input("Lastname <<== ")
        for char in lastname:
            if not char.isalpha():
                print(f"Sorry, invalid character: {char}")
                break
            else:
                pass
        else:
            if lastname == "ZZZ":
                quit()
            break

    # Makes sure only letters are entered as a first name
    while True:
        firstname = input("Firstname <<== ")
        for char in firstname:
            if not char.isalpha():
                print(f"Sorry, invalid character: {char}")
                break
            else:
                pass
        else:
            break

    if lastname.lower() in students.keys():
        # If the user is registered the system will tell the in which list they are
        print(f"\n{lastname.capitalize()} {students[lastname]['firstname'].capitalize()}")
        if students[lastname]["gpa"] >= 3.5:
            print("You are in the Dean's scholarship list\n")
        elif 3.25 <= students[lastname]["gpa"] < 3.5:
            print("You are in the Honor Roll scholarship list\n")
        else:
            print("Your GPA is not strong enough yet, keep working hard!\n")
    else:
        # If the user is new the system will ask for a GPA and add them to the system
        gpa = float(input("GPA <<== "))
        print("You have been added to our system, please sign in!\n")

        students[lastname] = {
            "firstname": firstname,
            "gpa": gpa
        }