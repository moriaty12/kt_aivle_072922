def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i
def solution(arr):
    answer = 1
    for i in range(len(arr)):
        answer=lcm(answer,arr[i])
    return answer

print(solution([2,6,8,14]))