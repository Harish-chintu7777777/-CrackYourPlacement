class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        def f(i,j):
            if i==0 and j==0:
                return grid[i][j]
            if i<0 or j<0:
                return 1e9
            if dp[i][j]!=-1:
                return dp[i][j]
            
            left=grid[i][j]+f(i-1,j)
            right=grid[i][j]+f(i,j-1)
            dp[i][j]=min(left,right)
            return dp[i][j]
        m,n = len(grid),len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        return f(m-1,n-1)
