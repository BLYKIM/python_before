def solution(price, money, count):
    answer = 0
    newprice = 0
    for c in range(1,count+1):
        newprice += price*c
    if newprice > money:
        answer = newprice - money

    return answer


price = 3
money = 20
count = 4

print(solution(price, money, count))
