class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        n = len(arr)
        left, right = [-1]*n, [n]*n
        stk = []
        for i in range(n):
            while(stk and arr[stk[-1]] >= arr[i]):
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n-1,-1,-1):
            while(stk and arr[stk[-1]] >= arr[i]):
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        print(left)
        print(right)
        res, mod = 0, 10**9 + 7
        for i in range(n):
            res += (i - left[i]) * (right[i] - i) * arr[i]
        return res % mod
