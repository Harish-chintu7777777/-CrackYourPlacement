class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # def f(ind,prev,dp):
        #     if ind>=n:
        #         return 0
        #     if dp[ind][prev+1]!=-1:
        #         return dp[ind][prev+1]
        #     l=0+f(ind+1,prev,dp)
        #     if prev==-1 or nums[ind]>nums[prev]:
        #         l=max(l,1+f(ind+1,ind,dp))                    TLE
        #     dp[ind][prev+1]=l
        #     return dp[ind][prev+1]
        # n=len(nums)
        # dp=[[-1]*len(nums) for j in range(len(nums)+1)]
        # return f(0,-1,dp)

        temp = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                temp[bisect_left(temp,nums[i])] = nums[i]
                
        return len(temp)
        

        
                
