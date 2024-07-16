class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        s,cnt = 0,0
        for i in nums:
            s += i
            r = s - k
            if r in d:
                cnt += d[r]
            if s in d:
                d[s] += 1
            else:
                d[s] = 1

        return cnt
        
