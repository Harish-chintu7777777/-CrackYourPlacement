class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
        stk = []
        rem = len(nums) - k
        res = []
        for i in nums:
            while(stk and rem and stk[-1] > i):
                stk.pop()
                rem -= 1
            stk.append(i)
        while(rem):
            stk.pop()
            rem -= 1
        return stk
