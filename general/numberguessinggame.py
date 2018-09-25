import random

print("Choose 2 numbers and I will pick a random number for you to guess\n")
lownum = int(input("Lower Number: "))
highnum = int(input("Higher Number: "))


def random_number_getter():
    if lownum < highnum:
        return random.randint(lownum, highnum)
    else:
        print("Please use the correct order")
        raise SystemExit


secret = random_number_getter()
guess = 1
while True:
    try:
        guess_number = int(input("Guess my Number! "))
        if guess_number != secret:
            if guess == 3:
                print("That's too bad, my Secret Number was", secret)
                break
            if guess_number < secret:
                print("Too low, try again!\n")
                guess += 1
            elif guess_number > secret:
                print("Too high, try again!\n")
                guess += 1
        else:
            print("You got it!!\n\nThe Secret Number was", secret)
            break
    except ValueError:
        print("Please enter a number")
