# 특정 원소가 속한 집합 찾기, 해당 노드의 루트 노드가 바로 부모 노드라 압축
import sys
sys.setrecursionlimit(10**6)
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v = int(input())
e = int(input())
parent = [0] * (v + 1)  # 부모 테이블 초기화하기

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 간선 정보 입력 받기
edges = []
result = 0
for i in range(e):
    a, b, weight = map(int, input().split())
    edges.append((weight, a, b))

# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며 최소 신장 트리 구성
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
