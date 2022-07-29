def sol(list_A,num_X):
    list=[]
    for i in range(len(list_A)):
        if list_A[i]<num_X:
            list.append(list_A[i])
    '''
    for j in range(len(list)):
        print(list[j],end='')
    return 0
    '''

    return list

print(sol([1,10,4,9,2,3,8,5,7,6],5))