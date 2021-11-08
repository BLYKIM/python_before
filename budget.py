def solution(d, budget):
    answer = 0
    d.sort()
    for dd in d:
        budget -= dd
        if budget < 0:
            break
        answer += 1
    return answer


d = [2, 2, 3, 3]
budget = 10

print(solution(d, budget))