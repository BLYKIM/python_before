'''
def solution(participant, completion):
    answer = ''

    for p in completion:
        participant.remove(p)
    answer = participant[0]
    return answer
''' # 효율성 O(n) O(n) 으로 실패


def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1] # 정렬 비교로 효울성 성공

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant,completion))