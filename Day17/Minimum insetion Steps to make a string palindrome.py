class Solution:
    def minInsertions(self, s: str) -> int:
        
        @cache
        def f(i,j):
            if i == j:
                return 0
            if i >= j:
                return 0
            if s[i] == s[j]:
                return f(i+1,j-1)
            else:
                return 1 + min(f(i+1,j),f(i,j-1))
        n = len(s)
        return f(0,n-1)
