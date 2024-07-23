class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxi = -1e9
        m = 1
        for i in nums:
            m *= i
            maxi = max(m,maxi)
            if m == 0:
                m = 1
        m = 1
        for i in nums[::-1]:
            m *= i
            maxi = max(maxi,m)
            if m == 0:
                m = 1
        return maxi


        
