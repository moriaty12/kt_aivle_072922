def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
cnt=0
for i in range(2,1001):
    if prime(i):
        #print(i,end='  ')
        cnt+=1

print(cnt)
