from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def f(ind):
            if ind < 0:
                return 0
            if ind == 0:
                return arr[0]
            if ind in memo:
                return memo[ind]
            pick = arr[ind] + f(ind - 2)
            notPick = f(ind - 1)
            memo[ind] = max(pick, notPick)
            return memo[ind]

        if not nums:
            return 0
        
        max_num = max(nums)
        arr = [0] * (max_num + 1)
        
        for num in nums:
            arr[num] += num
        
        memo = {}
        return f(max_num)
