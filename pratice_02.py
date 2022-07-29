def reverse():
    list=[]
    i=0
    print('print list revers')
    print('if you Enter "End" function is stop')

    while True:
        s=input(f'list[{i}] is .: ')
        if s=='End':
            break
        list.append(int(s))
        i+=1
    num=len(list)
    for k in range(num//2):
        list[k],list[num-k-1]=list[num-k-1],list[k]

    for j in range(num):
        print(f'list[{j}]={list[j]}')
    return list

reverse()