class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] % k
        cnt = 0
        d = {0:1}
        s = 0
        for i in nums:
            s += i
            rem = s%k
            if rem in d:
                cnt += d[rem]
            if rem in d:
                d[rem] += 1
            else:
                d[rem] = 1
        return cnt
            
