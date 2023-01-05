"""
00시 00분 00초부터 h시 59분 59초까지 3이 포함되는 모든 경우의 수를 출력합니다
5 -> 11475
"""
h = int(input())

count = 0
for i in range(h+1):  # 시
    for j in range(60):  # 분
        for k in range(60):  # 초
            if '3' in str(i) + str(j) + str(k):  # 'h0000내에 3이있으면 카운트
                count += 1
print(count)