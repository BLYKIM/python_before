def solution(lottos, win_nums):
    answer = []
    zeros = 0

    tmp = 0
    for i, l in enumerate(lottos):
        if l in win_nums:
            tmp += 1
        if l == 0:
            zeros += 1
    if not zeros and not tmp:
        answer.append(6)
    else:
        answer.append(7 - (tmp+zeros))
    if tmp == 0:
        answer.append(6)
    else:
        answer.append(7 - tmp)


    return answer

lottos={44, 1, 0, 0, 31, 25}
