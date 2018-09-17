
while True:
    try:
        penny = int(input("Number of pennies? "))
        nickel = int(input("Number of nickels? "))
        dime = int(input("Number of dimes? "))
        quarter = int(input("Number of quarters? "))
        total = (penny * .01) + (nickel * .05) + (dime * .1) + (quarter * .25)
        total = format(total, '.2f')
        print("Total: $"+total)
        break
    except ValueError:
        print('You must enter an integer :(')
