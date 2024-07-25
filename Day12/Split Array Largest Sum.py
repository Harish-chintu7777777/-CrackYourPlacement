class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def f(mid,k):
            curr = 0
            s = 1
            for i in range(len(nums)):
                if curr + nums[i] <= mid:
                    curr += nums[i]
                else:
                    s += 1
                    curr = nums[i]
            return s
        nums.sort()
        l,r = max(nums),sum(nums)
        while(l<=r):
            mid = (l+r) // 2
            v = f(mid,k)
            if v > k:
                l = mid + 1
            else:
                r = mid - 1
        return l
