def solution(n):
    answer = 0
    t = ''
    if n < 3:
        return n
    while n != 0:
        t = t + str(n % 3)
        n //= 3
    t = t[::-1]
    for i in range(len(t)):
        answer += (int(t[i])*(3**i))

    return answer

n = 125
print(solution(n))