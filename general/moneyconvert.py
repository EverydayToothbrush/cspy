
while True:
    try:
        exchange_rate = float(input("What is the current exchange rate? "))
        amt = float(input("What amount would you like to convert to US Dollars? "))

        print("You have " + format(amt * exchange_rate, '.2f') + " USD")
        break
    except ValueError:
        print("Use floats")
