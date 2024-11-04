class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ci = 0
        cj = 0
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        flag = 0
        answer = []
        visited = []

        for _ in range(len(matrix) * len(matrix[0])):
            visited.append((ci, cj))
            answer.append(matrix[ci][cj])
            if ci + di[flag] < 0 or ci + di[flag] > len(matrix) - 1 or cj + dj[flag] < 0 or cj + dj[flag] > len(matrix[0]) - 1 or (ci + di[flag], cj + dj[flag]) in visited:
                flag = (flag + 1) % 4
            
            ci += di[flag]
            cj += dj[flag]

        return answer