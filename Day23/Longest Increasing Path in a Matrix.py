class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def f(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            maxi = 1
            for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr,nc = i+r, j+c
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc] > matrix[i][j]:
                    maxi = max(maxi, 1 + f(nr,nc))
                    dp[(i,j)] = maxi

            return maxi
        m,n = len(matrix), len(matrix[0])
        maxi = 0
        dp = {}
        for i in range(m):
            for j in range(n):
                maxi = max(maxi, f(i,j))
        return maxi 
