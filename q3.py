def solution(store, customer):
    answer = []
    for i in range(len(customer)):
        for j in range(len(store)):
            if customer[i]==store[j]:
               customer[i]='yes'


    for k in range(len(customer)):
        if customer[k]!='yes':
            customer[k]='no'

    return customer

print(solution([2,3,7,8,9],[7,5,9]))