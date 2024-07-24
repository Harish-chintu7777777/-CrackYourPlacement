class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        d = {}
        l = 0
        maxi = 1
        for i in range(n):
            d[s[i]] = d.get(s[i],0) + 1
            while(i-l+1 - max(d.values()) > k):
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
            maxi = max(maxi,i-l+1)
        return maxi
            
