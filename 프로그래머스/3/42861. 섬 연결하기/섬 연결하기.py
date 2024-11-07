import sys
sys.setrecursionlimit(10**6)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    # 부모 테이블 초기화 (0부터 n-1까지)
    parent = [i for i in range(n)]
    
    # 비용을 기준으로 간선 리스트 정렬
    costs.sort(key=lambda x: x[2])
    
    # 비용이 적은 간선부터 순차적으로 확인하여 최소 스패닝 트리 구성
    for a, b, cost in costs:
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer
