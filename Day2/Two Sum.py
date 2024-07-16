class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            x=nums[i]
            y=target-nums[i]
            if x in d:
                return [d[x],i]
            else:
                d[y]=i
        
