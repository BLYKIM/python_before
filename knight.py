"""
8x8 체스판위의 나이트 이동가능 경우의 수 a-h, 1-8
"""
cp = input() # a1 -> 2

r = int(cp[1])
c = int(ord(cp[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

result = 0
for step in steps:
    next_r = r + step[0]
    next_c = c + step[1]

    if next_r >= 1 and next_r <= 8 and next_c >= 1 and next_c <= 8:
        result += 1
print(result)