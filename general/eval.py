running = ''
while running != 'Exit':
    running = input()
    if running != 'Exit':
        res = eval(running)
        print(res)
    else:
        break

