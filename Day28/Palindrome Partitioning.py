class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def f(ind, temp):
            
            if ind >= n:
                cv = temp.copy()
                res.append(cv)
                return
            curr = ''
            for i in range(ind, n):
                curr += s[i]
                if curr == curr[::-1]:
                    temp.append(curr)
                    f(i + 1, temp)
                    temp.pop()

        n = len(s)
        
        res = []
        f(0, [])
        return res

