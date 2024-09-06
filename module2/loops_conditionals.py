# Luis Velasquez | Loops and Conditionals

# 4.1
secret = 6
guess = 9

if guess < secret:
    print("Too low!")
elif guess > secret:
    print("Too high!")
else:
    print("Just right!")


# 4.2
small = True
green = True

if small:
    print("Cherry, Pea")
if green:
    print("Watermelon, Pumpkin")


# 6.1
lst = [3, 2, 1, 0]
for num in lst:
    print(num)


# 6.2
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("Too low!")
    elif number == guess_me:
        print("Found it!")
        break
    else:
        print("Oops!")
        break
    number += 1


# 6.3
guess_me = 5
number = range(10)

for num in number:
    if num < guess_me:
        print("Too low!")
    elif num == guess_me:
        print("Found it!")
    else:
        print("Oops!")
        break