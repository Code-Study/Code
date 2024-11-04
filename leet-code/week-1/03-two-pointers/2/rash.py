class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        last = len(height) - 1
        answer = 0
        while start <= last:
            answer = max(answer, min(height[start],height[last]) * (last - start ))
            if height[start] < height[last]:
                start += 1
            else:
                last -= 1

        print(start ,last)
        return answer
