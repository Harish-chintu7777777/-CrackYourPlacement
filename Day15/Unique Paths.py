class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def f(i,j,dp):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            top=f(i-1,j,dp)
            left=f(i,j-1,dp)
            dp[i][j]=top+left
            return dp[i][j]
        dp=[[-1]*(n) for j in range(m)]
        return f(m-1,n-1,dp)

       

        
