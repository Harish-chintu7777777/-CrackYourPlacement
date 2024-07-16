class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        i,j = 0,1
        while(i<=j and j<n):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
        return i+1
