class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        right = [n for i in range(n)]
        left = [-1 for i in range(n)]

        stk = []
        for i in range(n-1,-1,-1):
            while(stk and heights[stk[-1]] >= heights[i]):
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n):
            while(stk and heights[stk[-1]] >= heights[i]):
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        maxi = -1e9
        for i in range(n):
            maxi = max(maxi,(right[i]-left[i]-1)*heights[i])
        return maxi
        
