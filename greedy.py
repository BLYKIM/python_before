def solution(n, lost, reserve):
    answer = n
    tmp = []
    for l in lost:  # 여분을 가져오고 도난당한 학생
        if l in reserve:
            reserve.remove(l)
            tmp.append(l)
    for t in tmp:  # 중복제거 다른방법 찾기
        lost.remove(t)
    print('first lost = ', lost)
    print('first res = ', reserve)
    for l in lost:
        if l > 1 and l - 1 in reserve:
            reserve.remove(l - 1)
        elif l < n and l + 1 in reserve:
            reserve.remove(l + 1)
        else:
            answer -= 1
        print('lost= ', lost)
        print('reserve= ', reserve)
        print('')

    return answer

n = 12
lost = [1, 2, 3, 4, 8, 9, 10, 11]
reserve = [9, 10]

print(solution(n, lost, reserve)) # return값은 5