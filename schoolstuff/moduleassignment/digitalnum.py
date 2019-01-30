def horizontal_line(x):
    print('*' * x)


def vertical_line(x, y):
    for i in range(x):
        print(format('*', '>' + repr(y)))


def two_vertical_lines(x, y):
    for i in range(x):
        print("*" + format('*', '>' + repr(y)))


def number_0(x):
    horizontal_line(x)
    two_vertical_lines(3, x-1)
    horizontal_line(x)


def number_1(x):
    vertical_line(5, x)


def number_2(x):
    horizontal_line(x)
    vertical_line(1, x)
    horizontal_line(x)
    vertical_line(1, 0)
    horizontal_line(x)


def number_3(x):
    horizontal_line(x)
    vertical_line(1, x)
    horizontal_line(x)
    vertical_line(1, x)
    horizontal_line(x)


def number_4(x):
    two_vertical_lines(2, x-1)
    horizontal_line(x)
    vertical_line(2, x)


def number_5(x):
    horizontal_line(x)
    vertical_line(1, 0)
    horizontal_line(x)
    vertical_line(1, x)
    horizontal_line(x)


def number_6(x):
    horizontal_line(x)
    vertical_line(1, 0)
    horizontal_line(x)
    two_vertical_lines(1, x-1)
    horizontal_line(x)


def number_7(x):
    horizontal_line(x)
    vertical_line(4, x)


def number_8(x):
    horizontal_line(x)
    two_vertical_lines(1, x-1)
    horizontal_line(x)
    two_vertical_lines(1, x-1)
    horizontal_line(x)


def number_9(x):
    horizontal_line(x)
    two_vertical_lines(1, x-1)
    horizontal_line(x)
    vertical_line(2, x)


def plus(x):
    if x % 2 != 0:
        vertical_line(2, (x/2) + 1)
        horizontal_line(x)
        vertical_line(2, (x/2) + 1)
    else:
        vertical_line(2, x//2)
        horizontal_line(x)
        vertical_line(2, x//2)


def minus(x):
    horizontal_line(x)


def check_answer(x, y, z, a):
    if a == '+':
        return x + y == z
    elif a == '-':
        return x - y == z


