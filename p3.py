
def p3():
    list = []
    i = 0
    key=input(f'plz enter key :')


    while True:
        s = input(f'list[{i}] is .: ')

        if s == 'E':
            break
        list.append(int(s))
        i += 1

    for j in range(len(list)):
        if int(key)==list[j]:
            return j


    return -1

print(p3())

