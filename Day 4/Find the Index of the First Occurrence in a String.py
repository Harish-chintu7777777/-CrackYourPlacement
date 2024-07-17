class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n = len(haystack)
        k = len(needle)
        for i in range(n-k+1):
            c = 0
            for j in range(k):
                if haystack[i+j] == needle[j]:
                    c += 1
            if c == k:
                return i
        return -1
                
