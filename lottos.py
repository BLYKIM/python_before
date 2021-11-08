def solution(lottos, win_nums):
    answer = []
    zeros = 0

    tmp = 0
    for i in lottos:
        if i in win_nums:
            tmp += 1
        if i == 0:
            zeros += 1
    if not zeros and not tmp:
        answer.append(6)
    else:
        answer.append(7 - (tmp + zeros))
    if tmp == 0:
        answer.append(6)
    else:
        answer.append(7 - tmp)

    return answer


'''
lotto = [45, 4, 35, 20, 3, 9]
win_num = [20, 9, 3, 45, 4, 35]

print(solution(lotto, win_num))
'''

'''
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
'''

'''
def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
'''