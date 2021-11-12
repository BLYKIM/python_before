'''
keypad = [
[1, 2, 3],    # 00 01 02
[4, 5, 6],    # 10 11 12
[7, 8, 9],    # 20 21 22
['*', 0, '#'] # 30 31 32
]
'''
def hposition(number): # hand position을 return하는 함수
    keypad = [
        [1, 2, 3],  # 00 01 02
        [4, 5, 6],  # 10 11 12
        [7, 8, 9],  # 20 21 22
        ['*', 0, '#']  # 30 31 32
    ]
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == number:
                position = [i, j]
    return position

def solution(numbers, hand):
    answer = ''
    lpos = [3,0]
    rpos = [3,2]
    for n in numbers:
        if n in [1, 4, 7]: # 1, 4, 7일 때 왼손
            answer += 'L'
            lpos = hposition(n)
        if n in [3, 6, 9]: # 3, 6, 9일 때 오른손
            answer += 'R'
            rpos = hposition(n)
        if n in [2, 5, 8, 0]: # 2, 5, 8, 0일 때 가까운 손
            l = abs(hposition(n)[0] - lpos[0]) + abs(hposition(n)[1] - lpos[1])
            r = abs(hposition(n)[0] - rpos[0]) + abs(hposition(n)[1] - rpos[1])
            if l < r: # 왼손이 가까울 경우
                answer += 'L'
                lpos = hposition(n)
            if l > r: # 오른손이 가까울 경우
                answer += 'R'
                rpos = hposition(n)
            if l == r: # 거리가 같을 경우
                if hand == 'left': # 왼손잡이
                    answer += 'L'
                    lpos = hposition(n)
                if hand == 'right': # 오른손잡이
                    answer += 'R'
                    rpos = hposition(n)


    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]

hand = "right"


print(solution(numbers, hand))
# return값은 LRLLLRLLRRL
