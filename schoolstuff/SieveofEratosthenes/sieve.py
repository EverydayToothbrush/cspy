def eratos(x):
    sieve = ["P"] * (x + 1)
    for i in range(len(sieve)):
        if i == 0 or i == 1:
            sieve[i] = "N"
        elif sieve[i] == "P":
            for n in range(i+i, len(sieve), i):
                sieve[n] = "N"
    return sieve


def main():
    range_entry = int(input("Enter Number range: "))
    nums = []
    for i in range(len(eratos(range_entry))):
        if eratos(range_entry)[i] == "P":
            nums.append(i)
    for e in range(len(nums)):
        if e % 10 == 0:
            print()
        print(format(nums[e], ">3d"), end=" ")


main()
