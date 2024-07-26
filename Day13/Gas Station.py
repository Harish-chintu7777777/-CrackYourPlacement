class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        if sum(gas) - sum(cost) < 0:
            return -1

        ans = 0
        total = 0
        for i in range(n):
            total += (gas[i]-cost[i])
            if total < 0:
                ans = i+1
                total = 0
        return ans
