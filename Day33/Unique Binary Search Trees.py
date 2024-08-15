class Solution:
    def numTrees(self, n: int) -> int:
       
        @cache
        def unq(n):
            if n<=1:
                return 1
            if n==2:
                return 2
            k = 0
            for i in range(n):
                l = unq(i)
                r = unq(n-i-1)
                k+=l*r
            return k

        return unq(n)
