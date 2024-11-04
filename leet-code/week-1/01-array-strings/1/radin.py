class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        newMat = [row[:] for row in matrix]
        
        for i in range(0, n):
            for j in range(0, n):
                matrix[i][j] = newMat[n-1-j][i]
