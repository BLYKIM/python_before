def solution(answers):
    answer = []
    aa = [1, 2, 3, 4, 5]
    ba = [2, 1, 2, 3, 2, 4, 2, 5]
    ca = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == aa[i%5]:
            score[0] += 1
        if answers[i] == ba[i%8]:
            score[1] += 1
        if answers[i] == ca[i%10]:
            score[2] += 1
    mscore = max(score)
    for s in range(3):
        if score[s] == mscore:
            answer.append(s+1)

    return answer


answers = [1, 3, 2, 4, 2]

print(solution(answers))