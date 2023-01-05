"""
최대공약수 계산(유클리드 호제법)
두 자연수 A>B A를 B로나눈 나머지 R
이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다
GCD(192, 162)
"""

def GCD(a, b):
    if a%b == 0:
        return b
    return GCD(b, a%b)

print(GCD(162,192))