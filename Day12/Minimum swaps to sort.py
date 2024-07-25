class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        #Code here
        
        numIndx = [[nums[i],i] for i in range(len(nums))]
        numIndx.sort()
        i=0
        count = 0
        while i<len(nums):
            j = numIndx[i][1]
            if j==i:
                i+=1
                continue
            numIndx[i], numIndx[j] = numIndx[j], numIndx[i]
            count+=1
        return count
