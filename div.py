'''
다 필요없고 약수가 홀수개 == 제곱수 4 9 16 25 등
int(num ** 0.5) == num ** 0.5
'''

def div(num):
    cnt = 2
    if num == 1:
        return 1
    for i in range(2,num):
        if num%i == 0:
            cnt += 1
    return cnt


def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if div(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


left = 1
right = 2

print(solution(left, right))