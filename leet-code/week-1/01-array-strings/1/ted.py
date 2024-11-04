class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        ans = []
        
        for i in range(n):
            row = []
            for j in range(n):
                row.append(matrix[n-j-1][i])
            ans.append(row)

        # matrix를 변경시켜야 함 (matrix = ans는 matrix가 ans를 가르킬 뿐)
        for i in range(n):
            matrix[i] = ans[i]