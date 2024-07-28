class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def rec(heights):
            right = [len(heights) for i in range(len(heights))]
            stk = [-1]
            n = len(heights)

            for i in range(n - 1, -1, -1):
                while stk and heights[stk[-1]] >= heights[i]:
                    stk.pop()
                if stk:
                    right[i] = stk[-1]
                stk.append(i)

            stk = [-1]
            left = [-1 for i in range(n)]
            for i in range(n):
                while stk and heights[stk[-1]] >= heights[i]:
                    stk.pop()
                if stk:
                    left[i] = stk[-1]
                stk.append(i)

            maxArea = 0
            for i, height in enumerate(heights):
                width = (right[i] - left[i] - 1)
                area = width * height
                maxArea = max(maxArea, area)

            return maxArea

        
        m = 0
        hei = [0 for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    hei[j] += 1
                else:
                    hei[j] = 0
            m = max(rec(hei), m)

        return m
