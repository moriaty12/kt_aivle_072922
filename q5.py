

def solution(n, s):


    answer = []
    if n>s:
        answer= [-1]
    if s%2==0:
        answer=[s//2,s//2]
    if s%2==1:
        answer=[s//2,s//2+1]


    return answer

print(solution(2,87))