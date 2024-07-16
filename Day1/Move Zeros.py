class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
       
        i,j=0,1
        while(i<j and j<len(nums)):
            if nums[i]==0 and nums[j]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            elif nums[i]==0 and nums[j]==0:
                j+=1
            else:
                i+=1
                j+=1
        return nums

        
