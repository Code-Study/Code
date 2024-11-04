class Solution:    
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        self.m, self.n = len(matrix), len(matrix[0])

        self.dxys = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        self.cur_dir = 0
        self.visited = [
            [False for _ in range(self.n)]
            for _ in range(self.m)
        ]
        self.LAST_POS = (-1, -1)
        return self.simulate(matrix, 0, 0)
    
    def simulate(self, matrix: list[list[int]], x: int, y: int):
        self.visited[x][y] = True
        nx, ny = self.get_next_pos(x, y)
        if (nx, ny) == self.LAST_POS:
            return [matrix[x][y]]
        result = self.simulate(matrix, nx, ny)
        return [matrix[x][y]] + result

    def in_range(self, x, y):
        return 0<=x<self.m and 0<=y<self.n

    def can_go(self, x, y):
        return self.in_range(x, y) and not self.visited[x][y]

    def get_next_pos(self, x, y) -> tuple[int, int]:
        for _ in range(4):
            dx, dy = self.dxys[self.cur_dir]
            nx, ny = x + dx, y + dy
            if self.can_go(nx, ny):
                return nx, ny
            else:
                self.cur_dir = (self.cur_dir + 1) % 4
        return self.LAST_POS