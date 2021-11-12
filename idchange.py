'''te = '....asdjkh.....sadjalkd.sadoj..asdhas...'
tmp = te
print(tmp)
while '..' in tmp:
    tmp = tmp.replace('..', '.')
    print(tmp)

print(tmp)

tmp = tmp.strip('.')

print(tmp)'''


def solution(new_id):
    tmp = new_id
    tmp = tmp.lower()  #1단계 소문자 치환
    for w in tmp:
        if w.isalnum() or w in['-', '_', '.']:
            pass
        else:
            tmp = tmp.replace(w, '', 1)  #2단계 특문없애기
    while '..' in tmp:
        tmp = tmp.replace('..', '.')  #3단계 마침표 연속 없애기
    tmp = tmp.strip('.')  #4단계 양 끝 마침표 없애기
    if not tmp:
        tmp = 'a'  #5단계 빈 문자열이면 a대입
    if len(tmp) >= 16:
        tmp = tmp[:15]  #6단계 초과 문자수 삭제 (0~14까지 15자)
        tmp = tmp.rstrip('.')
    while len(tmp) < 3:
        tmp += tmp[-1]  #7단계 맨 뒤 문자 붙이기 (3자가 될 때 까지)


    return tmp

new_id = '...!@BaT#*..y.abcdefghijklm'

print(solution(new_id))
