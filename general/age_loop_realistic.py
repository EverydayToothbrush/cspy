while True:
    try:
        age = int(input("Enter your age: "))
        if 0 <= age <= 101:
            print("Your age is", age)
            break
        else:
            print("I am quite certain you are not that age.")
            continue
    except ValueError:
        print("Enter a number please")
