class Solution(object):
    def maxArea(self, height):
        st = 0
        ed = len(height) - 1
        maxV = 0
        
        while st <= ed:
            area = min(height[st], height[ed]) *  (ed - st)
            maxV = max(area, maxV)
            
            if height[st] < height[ed]:
                st += 1
            else:
                ed -= 1
            
        return maxV
