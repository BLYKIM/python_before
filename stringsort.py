"""
AD39KGI84 등과 같은 입력에서 알파벳은 오름차순으로 앞에쓰고
숫자는 더해서 뒤에 붙임
"""

data = input()
result = []
num = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        num += int(x)

result.sort()

if num != 0:  # 숫자가 하나라도 존재하면 가장 뒤에 append(str로)
    result.append(str(num))

print(''.join(result))  # 리스트를 문자열로 변환하여 출력