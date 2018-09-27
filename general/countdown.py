import time
i = int(input("Enter a number greater than 0 to start the countdown: "))
print()
while i > 0:
    time.sleep(1)
    print(i, "#" * i)
    i -= 1
