import random

def main():
    file_name = input("File path: ")
    file = open(file_name, 'r')

    all_lines = []
    for line in file:
        line = line.strip()
        all_lines.append(line)
    file.close()
    choose = random.choice(all_lines)
    print(choose)


main()