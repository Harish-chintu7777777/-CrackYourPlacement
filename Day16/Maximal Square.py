class Solution(object):
    def maximalSquare(self, mat):
        m,n = len(mat),len(mat[0])
        ans = 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if mat[i][j] == '1':
                        dp[i][j] = 1
                else:
                    if mat[i][j] == '1':
                        dp[i][j] = min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1])) + 1
                    
                ans = max(dp[i][j], ans)
        
        return ans*ans
                
