class Solution:
    def eraseOverlapIntervals(self, i: List[List[int]]) -> int:
        if len(i)==1:
            return 0
        n=len(i)
        i.sort(key = lambda x: x[1])
        p = 0
        cnt = 0
        for k in range(1,n):
            if i[k][0] >= i[p][1]:
                p = k
                cnt += 1
        return n - cnt - 1

