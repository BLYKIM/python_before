def solution(record):
    answer = []
    user = {}
    state = []
    for rec in record:
        sci = rec.split(' ')

        if sci[0] == 'Enter' and sci[1] not in user:
            user[sci[1]] = sci[2]
        elif sci[0] == 'Enter' and sci[1] in user:
            user[sci[1]] = sci[2]

        if sci[0] != 'Change':
            state.append((sci[0],sci[1]))
        else:
            user[sci[1]] = sci[2]
    for s in state:
        if s[0] == 'Enter':
            answer.append(user[s[1]] + "님이 들어왔습니다.")
        if s[0] == 'Leave':
            answer.append(user[s[1]] + "님이 나갔습니다.")


    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

#result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
