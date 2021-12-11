def solution(s):
    answer = []
    cnt = 1
    for i in range(1, (len(s) // 2) + 1):  #끊는 단위
        zstr = ""

        for j in range(0, len(s), i):  #비교 단위

            if s[j:j+i] != s[j+i:j+i+i]:
                if cnt > 1:
                    zstr = zstr + str(cnt) + s[j:j+i]
                else:
                    zstr = zstr + s[j:j+i]
                cnt = 1
            else:
                cnt += 1
        answer.append(zstr)

    print(answer)
    minans = len(s)
    for i in answer:
        if len(i) < minans:
            minans = len(i)
    return minans

s = "xxxxxxxxxxyyy"
print(solution(s))