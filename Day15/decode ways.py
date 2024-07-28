class Solution:
    def numDecodings(self, s: str) -> int:
        
        def f(ind):

            if ind >= n:
                return 1
            pick,not_pick = 0,0
            if s[ind] != '0':
                not_pick = f(ind+1)
            if ind+1<n and (s[ind] == '1' or (s[ind]>='2' and s[ind] <= '6')):
                pick = f(ind+2)
            dp[ind] = pick + not_pick
            return dp[ind]
        dp = {}
        n = len(s)
        return f(0)
