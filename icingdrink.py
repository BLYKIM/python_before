"""
NxM 크기 얼음 틀
구멍이 뚫린 부분 0 칸막이 존재 부분 1
구멍이 뚫린 부분끼리 서로 연결되어있음
얼음 틀 모양일때 총 아이스크림의 개수를 구하는 프로그램
예시 4x5
00110
00011
11111
00000
일 때 3개
"""

#dfs 혹은 bfs로 연결되어있는지 해결
#dfs

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x>= n or y<= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# N 과 M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)