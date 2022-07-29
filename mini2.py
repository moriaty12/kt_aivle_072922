
def reverse():
    list=[]
    print("print list revers")
    num =int(input('enter number.:  '))

    for i in range(num):
        list.append(int(input(f'plz enter list[{i}]:  ')))

    for k in range(num//2):
        list[k],list[num-k-1]=list[num-k-1],list[k]
        #print(list)

    #list=asd(list)
    for j in range(num):
        print(f'list[{j}]={list[j]}')

    return 0

reverse()