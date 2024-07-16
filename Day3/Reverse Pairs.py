class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge(lrr,rrr):
            i,j = 0,0
            while(i<len(lrr) and j<len(rrr)):
                if lrr[i] > 2*rrr[j]:
                    cnt[0] += len(lrr) - i
                    j += 1
                else:
                    i += 1
            res = []
            i,j = 0,0
            while(i<len(lrr) and j<len(rrr)):
                if lrr[i] < rrr[j]:
                    res.append(lrr[i])
                    i += 1
                else:
                    res.append(rrr[j])
                    j += 1
            return res + lrr[i:] + rrr[j:]


        
        cnt = [0]
        n = len(nums)
        def divide(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            l = divide(arr[:mid])
            r = divide(arr[mid:])
            return merge(l,r)
        nums = divide(nums)
        return cnt[0]
