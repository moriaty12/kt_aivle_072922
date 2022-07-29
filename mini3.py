def cnt_w(list,key):
    i=0
    cnt=0
    while True:
        cnt+=1
        if i==len(list):
            return (i,cnt)
        cnt+=1
        if list[i]==key:

            return (i,cnt)
        i+=1

def cnt_s(list,key):
    i=0
    cnt=0

    list_copy = list.copy()
    list_copy.append(key)
    while True:
        cnt+=1
        if list_copy[i] == key:


            break
        i += 1
    return (-1,cnt) if i==len(list) else (i,cnt)


def func(list,key):


    print("whlie= :",cnt_w(list,key))
    print("sent= :", cnt_s(list,key))
    return 0


func([2,5,1,3,9,6,7],7)