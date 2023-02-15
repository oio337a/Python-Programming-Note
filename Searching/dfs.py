# ------------------------------ #
'''
  case 1 : graph
'''


def dfs(graph, v, visited):
    # 현재 노드들 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
         [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9
dfs(graph, 1, visited)


# ---------------------------------------------------------- #
'''
  case 2 : 2차원 배열
'''

n, m = map(int, input().split())
# 2차원 리스트 맵 입력 받기
graph = [list(map(int, input())) for _ in range(n)]

# DFS로 특정한 노드를 방문한 뒤에 연결되 ㄴ모든 노드들도 방문


def dfs(x, y):
    # 주어진 범위를 벗어나면 재귀 탈출
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1  # 방문 체크
        # 상, 좌, 하, 우 체크
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True
    return False


count = 0

for x in range(n):
    for y in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(x, y) == True:
            count += 1
print(count)
