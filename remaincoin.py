"""
손님에게 거슬러 주어야 할 돈 N
N은 항상 10의 배수
500 100 50 10 동전의 최소 개수
"""


def remain(n):
    cnt = 0
    coins = [500, 100, 50, 10]

    for coin in coins:
        if n >= coin:
            cnt += (n // coin)
            n %= coin

    return cnt


n = 1260

print(remain(n))
