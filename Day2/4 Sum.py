class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        res = set()
        nums.sort()
        for ind,val in enumerate(nums):
            for j in range(ind+1,n):
                l,r = j+1,n-1
                while(l<r):
                    ss = val + nums[j] + nums[l] + nums[r]
                    if ss < target:
                        l += 1
                    elif ss > target:
                        r -= 1
                    else:
                        res.add((val,nums[j],nums[l],nums[r]))
                        l += 1
                        while(nums[l] == nums[l-1] and l<r):
                            l += 1
        return list(res)
