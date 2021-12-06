import random

top_of_range = input("Type a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please Type A Number Larger Than 0 ")
        quit()
else:
    print("Please Type A Number ")
random_number = random.randrange(0, 11)  # random number from 0 to 10
# print(random.randint(0, 10)) #random number from 0 to 10

guesses = 0

while True:
    guesses += 1
    user_guess = input("Type a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please Type A Number ")
        continue

    if user_guess == random_number:
        print("Yeahhh! You Got It Right ")
        break
    elif user_guess > random_number:
        print("You Are Above The Number ")
    else:
        print("You Are Below The Number ")

print("You Got Right Guess In ", guesses, " Chances")


