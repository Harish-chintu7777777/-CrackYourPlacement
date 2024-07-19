class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache
        def f(i,j):
            if j<0:
                return 1
            if i<0:
                return 0
            p1 = 0
            p2 = 0
            if s[i]==t[j]:
                p1 = f(i-1,j-1) + f(i-1,j)
            else:
                p2 = f(i-1,j)
            return p1+p2
        m=len(s)
        n=len(t)
        return f(m-1,n-1)
