n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k
result += (n - 1)
print(result)


'''
def until1(n, k):
    cnt = 0
    while n!= 1:
        if n%k == 0:
            n //= k
            cnt += 1
        else:
            n -= 1
            cnt += 1
    return cnt


n = 25
k = 3

print(until1(n,k))
'''