# 다익스트라 

''' 1. 구현 간단하지만 속도 느린 버전 '''
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 방문 체크 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n + 1)

# 간선 정보 입력 받기
for _ in range(m):
	# a 에서 b로 갈때 드는 비용 c
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_samllest_node():
	min_value = INF
	index = 0
	for i in range(1, n + 1):
		if distance[i] < min_value and not visited[i]:
			min_value = distance[i]
			index = i
	return index

def dijkstra(start):
	