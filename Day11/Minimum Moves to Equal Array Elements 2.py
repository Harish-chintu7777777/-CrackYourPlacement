class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        x = max(nums) - min(nums)
        x = x//2
        n = len(nums)

        cnt = 0
        for i in nums:
            cnt += abs(x-i)
        nums.sort()
        m = nums[n//2]
        c1 = 0
        for i in nums:
            c1 += abs(i-m)
        return min(cnt,c1)
