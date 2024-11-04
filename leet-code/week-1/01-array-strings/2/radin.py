class Solution(object):    
    def rotate(self, idx):
        return (idx + 1) % 4
    
    
    def inRange(self, x, y, X, Y):
        return 0 <= x < X and 0 <= y < Y
    
    
    def spiralOrder(self, matrix):
        direction = [[0,1], [1,0], [0,-1], [-1,0]]
        ans = [matrix[0][0]]
        
        X = len(matrix)
        Y = len(matrix[0])
        
        visited = [[False for _ in range(Y)] for _ in range(X)]
        d = 0
        idx = 1
        x, y = 0, 0
        visited[x][y] = True
        
        while idx < X * Y:
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            
            if not self.inRange(nx, ny, X, Y):
                d = self.rotate(d)
                nx = x + direction[d][0]
                ny = y + direction[d][1]
            if self.inRange(nx, ny, X, Y) and visited[nx][ny]:
                d = self.rotate(d) 
                nx = x + direction[d][0]
                ny = y + direction[d][1]
            
            visited[nx][ny] = True
            ans.append(matrix[nx][ny])
        
            x = nx
            y = ny
            idx += 1
          
        return ans
