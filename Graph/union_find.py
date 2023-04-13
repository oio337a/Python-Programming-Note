# https://www.acmicpc.net/problem/16562
# 친구비
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
costs = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]

def find(target): # 나와 연결된 노드 중 최상위 노드 탐색
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b): # 새로 입력된 노드 정보를 받아 부모노드와 연결
    a = find(a)
    b = find(b)
    if a != b:
        if costs[a] <= costs[b]:
            parent[b] = a
        else:
            parent[a] = b
for i in range(m):
    v, w = map(int, input().split())
    union(v, w)
ans = 0
for idx, root in enumerate(parent):
    if idx == root:
      ans += costs[idx]
if ans <= k:
    print(ans)
else:
    print("Oh no")