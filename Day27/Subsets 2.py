class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def f(ind, l):
            if ind >= n:
                curr = l.copy()
                curr = sorted(curr)
                res.append(tuple(curr))
                return
            l.append(nums[ind])
            f(ind+1, l)
            l.pop()
            f(ind+1, l)
        n = len(nums)
        res = []
        f(0,[])
        return sorted(set([] + res))
