class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def helper(i, j):
            if i > j:
                return 0
            if i == j:
                dp[i][j] = 1
                return dp[i][j]
            if dp[i][j] != -1:
                return dp[i][j]

            mod = 10**9 + 7

            if s[i] == s[j]:
                low, high = i + 1, j - 1
                while low <= high and s[low] != s[i]:
                    low += 1
                while low <= high and s[high] != s[i]:
                    high -= 1

                if low > high:
                    dp[i][j] = 2 * helper(i + 1, j - 1) + 2
                elif low == high:
                    dp[i][j] = 2 * helper(i + 1, j - 1) + 1
                else:
                    dp[i][j] = 2 * helper(i + 1, j - 1) - helper(low + 1, high - 1)
            else:
                dp[i][j] = helper(i + 1, j) + helper(i, j - 1) - helper(i + 1, j - 1)

            return dp[i][j] % mod

        return helper(0, n - 1)
