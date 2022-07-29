def solution(lottos, win_nums):
    answer = [0,0]
    cnt_right=0
    cnt_wrong=0
    cnt_zero=0
    for j in range(len(lottos)):
        if lottos[j]==0:
            cnt_zero+=1
    for i in range(len(win_nums)):
        for k in range(len(lottos)):
            if lottos[k]==win_nums[i]:
                cnt_right+=1
    if cnt_zero==6:
        answer=[1,6]

    elif cnt_zero==0 and cnt_right==0:
        answer=[6,6]

    else:
        if cnt_right==0 or cnt_right==1:
            answer[1]=6
        else:
            answer[1]=7-cnt_right
            answer[0]=7-cnt_right-cnt_zero



    return answer

print(solution(	[44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))