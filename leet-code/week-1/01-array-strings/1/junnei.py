class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for x in range(n//2):
            for y in range((n+1)//2):
                matrix = self.rotate_elements(matrix, x, y, n)
    
    def rotate_elements(self, matrix: list[list[int]], x: int, y: int, n: int) -> list[list[int]]:
        temp = matrix[x][y]
        for _ in range(4):
            x, y = self.get_pos(x, y, n)
            temp, matrix[x][y] = matrix[x][y], temp
        return matrix

    def get_pos(self, x: int, y: int, n: int) -> tuple[int, int]:
        center = (n-1)/2
        dx, dy = center - x, center - y
        nx, ny = center - dy, center + dx
        return int(nx), int(ny)