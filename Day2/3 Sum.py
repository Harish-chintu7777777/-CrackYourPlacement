class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        for ind,val in enumerate(nums):
            l,r = ind+1,n-1
            while(l<r):
                ss = val + nums[l] + nums[r]
                if ss > 0:
                    r -= 1
                elif ss < 0:
                    l += 1
                else:
                    res.add((val,nums[l],nums[r]))
                    l += 1
                    while(nums[l] == nums[l-1] and l<r):
                        l += 1
        return list(res)
                
