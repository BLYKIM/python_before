def solution(N, stages):  # N스테이지 중 stages에 머무른 이용자
    answer = []  # 딕셔너리 이용하는게 편함
    fail = []
    user = len(stages) # 유저 수
    for i in range(N):
        if user == 0:
            fail.append(0)
        else:
            fail.append(stages.count(i+1) / user)
            user -= stages.count(i+1)

    for t in range(N):
        maxfail = fail.index(max(fail))
        answer.append(maxfail + 1)
        fail[maxfail] = -1

    return answer


N = 5
stages = [2, 2, 2, 2, 2]
print(solution(N, stages))