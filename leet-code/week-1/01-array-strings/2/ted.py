class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # 오른쪽, 아래, 왼쪽, 위
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        m, n = len(matrix), len(matrix[0])
        res = []
        visited = [[False] * n for _ in range(m)]
        
        # 초기 위치와 방향 설정
        x, y, direction = 0, 0, 0
        
        # 전체 요소의 개수만큼 반복
        for _ in range(m * n):
            res.append(matrix[x][y])
            visited[x][y] = True
            
            # 다음 위치 계산
            nx, ny = x + dx[direction], y + dy[direction]
            
            # 행렬에 포함되면서 not visited
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                x, y = nx, ny   # 다음 위치로 이동
            else:   # 포함안되면 방향 전환
                direction = (direction + 1) % 4     # 방향 전환
                x, y = x + dx[direction], y + dy[direction]
        
        return res