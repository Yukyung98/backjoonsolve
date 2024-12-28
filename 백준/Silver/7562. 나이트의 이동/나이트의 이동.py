from collections import deque

directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
              (1, 2), (1, -2), (-1, 2), (-1, -2)]

def bfs(l, start, end):
    # 시작 지점과 목표 지점이 같으면 0
    if start == end:
        return 0

    # 방문 처리 배열
    visited = [[False] * l for _ in range(l)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, steps = queue.popleft()

        # 8방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                # 목표 지점에 도달하면 종료
                if (nx, ny) == end:
                    return steps + 1
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))
    
    return -1  # 목표에 도달할 수 없으면 -1 반환 (이 문제에서는 항상 도달 가능)

def main():
    t = int(input())  # 테스트 케이스 수
    
    for _ in range(t):
        l = int(input())  # 체스판 크기
        start = tuple(map(int, input().split()))  # 시작 지점
        end = tuple(map(int, input().split()))  # 목표 지점
        
        # BFS를 호출하여 최소 이동 횟수를 계산
        print(bfs(l, start, end))

# 입력 받기
main()
