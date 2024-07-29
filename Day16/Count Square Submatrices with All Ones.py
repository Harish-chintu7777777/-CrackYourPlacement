class Solution:
    def countSquares(self, arr: List[List[int]]) -> int:
        n = len(arr)
        m = len(arr[0])
        dp = [[0] * m for _ in range(n)]

        for j in range(m):
            dp[0][j] = arr[0][j]
        for i in range(n):
            dp[i][0] = arr[i][0]

        for i in range(1, n):
            for j in range(1, m):
                if arr[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])

        s = 0
        for i in range(n):
            for j in range(m):
                s += dp[i][j]
        return s






