class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
       answer = list(map(list, zip(*matrix[::-1])))
       for i in range(len(answer)):
        for j in range(len(answer[0])):
            matrix[i][j] = answer[i][j]