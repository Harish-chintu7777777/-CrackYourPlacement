class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def f(ind,buy):
            if ind >= n:
                return 0
            if (ind,buy) in dp:
                return dp[(ind,buy)]
            p = 0
            if buy:
                p = max(-prices[ind]+f(ind+1,0), f(ind+1,1))
            else:
                p = max(prices[ind]+f(ind+1,1), f(ind+1,0))
            dp[(ind,buy)] = p
            return p
        n = len(prices)
        dp = {}
        return f(0,1)
