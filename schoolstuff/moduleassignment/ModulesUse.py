def main():
    import digitalnum
    import random

    numquest = int(input("How many problems would you like to attempt? "))
    while numquest <= 0:
        print("Invalid number! Try again.\n")
        numquest = int(input("How many problems would you like to attempt? "))

    width = int(input("How wide do you want your digits to be? 5-10: "))
    while not 5 <= width <= 10:
        print("Invalid width! Try again.\n")
        width = int(input("How wide do you want your digits to be? 5-10: "))

    print("\nHere we go!\n")

    correct = 0
    for i in range(numquest):
        print("What is . . .\n")

        nums = {
            '0': digitalnum.number_0,
            '1': digitalnum.number_1,
            '2': digitalnum.number_2,
            '3': digitalnum.number_3,
            '4': digitalnum.number_4,
            '5': digitalnum.number_5,
            '6': digitalnum.number_6,
            '7': digitalnum.number_7,
            '8': digitalnum.number_8,
            '9': digitalnum.number_9,
            '+': digitalnum.plus,
            '-': digitalnum.minus
        }

        operation = ['+', '-']
        op = random.randint(0, 1)
        pm = operation[op]
        first = random.randint(0, 9)
        second = random.randint(0, 9)
        nums[str(first)](width)
        print()
        nums[pm](width)
        print()
        nums[str(second)](width)
        answer = int(input("= "))
        if digitalnum.check_answer(first, second, answer, pm):
            print("Correct!\n")
            correct += 1
        else:
            print("Sorry, that's not correct.\n")
    print("You got", correct, "out of", numquest, "correct!")


main()