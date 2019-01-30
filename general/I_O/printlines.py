def main():
    file_name = input('Enter file name: ')
    file = open(file_name, "r")
    wcw = file.read()
    file.close()
    print(wcw)

main()
