def solution(arr):
    answer=[]

    answer=arr.remove(min(arr))

    if not arr:
        answer =[-1]
    else:
        answer=arr
    return answer