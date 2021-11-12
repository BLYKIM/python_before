import datetime  # date time 안쓸거면 31 29 31 30 31 30 31 31 30 31 30 31 더하기


def solution(a, b):
    answer = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return answer[datetime.date(2016, a, b).weekday()]


a = 5
b = 24
print(solution(a, b))
