n = int(input())
plans = input().split()
x = 1
y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(moves)):
        if plan == moves[i]:
            nx = x + dx[i]
            ny = x + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x = nx
    y = ny

print(x, y)