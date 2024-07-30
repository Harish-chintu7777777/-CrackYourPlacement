from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @lru_cache(None)
        def f(ind, buy, k):
            if ind >= len(prices) or k == 0:
                return 0
            if buy:
                p1 = -prices[ind] + f(ind + 1, 0, k)
                p2 = f(ind + 1, 1, k)
                return max(p1, p2)
            else:
                p1 = prices[ind] + f(ind + 1, 1, k - 1)
                p2 = f(ind + 1, 0, k)
                return max(p1, p2)

        return f(0, 1, k)
