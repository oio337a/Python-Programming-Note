# ------------------------------ #
'''
  case 1 : graph
'''

from collections import deque


def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    que = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌때 까지 반복
    while que:
        # 큐에서 하나의 원소를 뽑아 출력
        v = que.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
         [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9
bfs(graph, 1, visited)


# ---------------------------------------------------------- #
'''
  case 2 : 2차원 배열
'''


# n * m 입력받기
n, m = map(int, input().split())
# n * m 보드 입력받기
board = [list(map(int, input())) for _ in range(n)]
# 큐 생성
que = deque()
que.append((0, 0))  # 시작값 세팅
# 우, 하, 상, 좌
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

while que:
    # 탐색할 좌표 꺼내기
    x, y = que.popleft()
    for i in range(4):
        # 4방 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        # board 벗어나는 경우 무시
        if 0 > nx or nx >= n or 0 > ny or ny >= m:
            continue
        # 방문하지 않은 곳이면서 갈 수 있는 곳 이면
        if board[nx][ny] == 1:
            # 전 값에 + 1 추가
            board[nx][ny] = board[x][y] + 1
            que.append((nx, ny))  # 다음 탐색할 좌표 추가

# n, m 좌표 출력하기
print(board[n - 1][m - 1])
