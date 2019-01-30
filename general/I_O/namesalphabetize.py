def main():
    file = open('./text-files/Text Files/names.txt', 'r')
    nameslet = file.read()
    names = nameslet.split('\n')
    names.sort()
    # alpha = []
    # for n in names:
    #     alpha.append(n)
    # alpha.sort()
    file.close()
    # print(*alpha, sep='\n')
    print(*names, sep='\n')


main()