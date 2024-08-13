from typing import List
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def __init__(self):
        self.prefixSum = [0]
        self.dp = {}

    def rec(self, stones: List[int], i: int, j: int, piles: int) -> int:
        if (i, j, piles) in self.dp:
            return self.dp[(i, j, piles)]

        if i >= j:
            return 0
        
        mini = float('inf')
        for k in range(i, j, piles - 1):
            tempAns = self.rec(stones, i, k, piles) + self.rec(stones, k + 1, j, piles)
            mini = min(tempAns, mini)
        
        if (j - i) % (piles - 1) == 0:
            mini += self.prefixSum[j + 1] - self.prefixSum[i]
        
        self.dp[(i, j, piles)] = mini
        return mini

    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        
        if (n - 1) % (k - 1) != 0:
            return -1
        
        for i in stones:
            self.prefixSum.append(self.prefixSum[-1] + i)
        
        return self.rec(stones, 0, n - 1, k)
