class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = 10001
        start = [0 for _ in range(n)]
        end = [0 for _ in range(n)]
        for i, j in intervals:
            start[i] += 1
            end[j] += 1
        
        answer = list()
        
        count = 0
        result = list()
        for i in range(n):
            if start[i] != 0:
                count += start[i]
                if count > 0 and len(result) == 0:
                    result.append(i)
            if end[i] != 0:
                count -= end[i]
                if count == 0:
                    result.append(i)
                    answer.append(result)
                    result = list()
        return answer