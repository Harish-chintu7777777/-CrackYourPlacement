class Solution:
    def solve(self, n, k, stalls):
        def f(mid):
            cnt = 1
            last = stalls[0]
            for i in range(1, n):
                if stalls[i] - last >= mid:
                    last = stalls[i]
                    cnt += 1
            return cnt

        stalls.sort()
        l, r = 1, stalls[-1] - stalls[0]
        answer = 0

        while l <= r:
            mid = (l + r) // 2
            v = f(mid)
            if v >= k:
                answer = mid
                l = mid + 1
            else:
                r = mid - 1
        return answer
