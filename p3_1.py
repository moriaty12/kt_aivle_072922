def seq_search_for(a, key):
    for i in range(len(a)):
        if a[i] == key:

            return i
    return -1
def p3():
    list = []
    i = 0
    key=input(f'plz enter key :')

    print('print list revers')
    print('if you Enter "End" function is stop')

    while True:
        s = input(f'list[{i}] is .: ')

        if s == 'End':
            break
        list.append(s)
        i += 1



    return seq_search_for(list,key)


print(p3())