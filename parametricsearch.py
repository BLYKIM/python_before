# 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화문제
# 이진탐색을 이용
"""
19 14 10 17cm인 떡 절단기높이 15
15 14 10 15, 잘린떡 4 0 0 2 손님은 6cm을 가져감?
손님이 요청한 길이가 M
적어도 M만큼의 떡을 얻기위해 절단기에 설정할 수 있는 높이의 최댓값
"""
# 입력예시 4 6 / 19 15 10 17, 출력 15

# 현재 높이로 자르면 조건을 만족할 수 있는가?

# 떡의 개수와 요청한 떡의 길이 입력
n, m = map(int, input().split(' '))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점
start = 0
end = max(array)

# 이진 탐색 수행 (반복)
result = 0
while(start<= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽부분)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분할 경우 덜 자르기 (오른쪽부분)
    else:
        result = mid #최대한 덜 잘랐을 때가 정답이므로, 여기서 result 기록
        start = mid + 1

print(result)