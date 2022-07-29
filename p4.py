def seq_search_for(a, key):
    for i in range(len(a)):
        if a[i] == key:

            return i
    return -1
def min_of(a):
    minimum=a[0]
    for i in range(1,len(a)):
        if a[i]<minimum:
            minimum=a[i]
    return minimum

def max_of(a):
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

def p4():
    list = []
    i = 0


    print('print list ')
    print('if you Enter "End" function is stop')

    while True:
        s = input(f'list[{i}] is .: ')

        if s == 'End':
            break
        list.append(int(s))
        i += 1
    max_num=max_of(list)
    min_num=min_of(list)
    return seq_search_for(list,min_num),seq_search_for(list,max_num)

print(p4())