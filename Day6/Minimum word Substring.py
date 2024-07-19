class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        d = Counter()
        d1 = Counter(t)
        have, req = 0, len(d1)
        l = 0
        mini = float('inf')
        ind = 0
        for r in range(len(s)):
            d[s[r]] += 1
            
            if s[r] in d1 and d[s[r]] == d1[s[r]]:
                have += 1
                
            while have == req:
                if (r - l + 1) < mini:
                    mini = r - l + 1
                    ind = l
                
                d[s[l]] -= 1
                if s[l] in d1 and d[s[l]] < d1[s[l]]:
                    have -= 1
                l += 1
        
        return s[ind:ind+mini] if mini != float('inf') else ""

