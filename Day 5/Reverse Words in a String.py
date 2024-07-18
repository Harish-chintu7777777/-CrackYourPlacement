class Solution:
    def reverseWords(self, s: str) -> str:
        
        n = len(s)
        res = []
        s = s.split()
        s=s[::-1]
        return " ".join(s)
