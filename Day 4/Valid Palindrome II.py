class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i,j = 0,n-1
        if s == s[::-1]:
            return True
        while(i<j):
            if s[i] != s[j]:
                x,y = s[:i],s[i+1:]
                if x+y == (x+y)[::-1]:
                    return True
                x,y = s[:j],s[j+1:]
                if x+y == (x+y)[::-1]:
                    return True
                else:
                    return False
            else:
                i += 1
                j -= 1
        return False
