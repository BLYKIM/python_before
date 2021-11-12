def solution(board, moves):
    answer = 0
    tboard = board
    basket = []
    r = 1
    for m in moves:
        n = 0
        while tboard[n][m - 1] == 0:
            n += 1
            if n == len(tboard):
                n -= 1
                break
        if tboard[n][m - 1] != 0:
            basket.append(tboard[n][m - 1])
        tboard[n][m - 1] = 0

    print(basket)
    while r < len(basket):
        if basket[r - 1] == basket[r]:
            basket = basket[:r - 1] + basket[r + 1:]
            r = 0
            answer += 2
        r += 1

    return answer

b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]

move = [1,5,3,5,1,2,1,4] #result = 4

print(solution(b, move))
