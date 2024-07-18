class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        
        d = {}
        for i in s:
            v = "".join(sorted(i))
            if v not in d:
                d[v] = [i]
            else:
                d[v] += [i]
        res = []
        for i in d:
            res.append(d[i])
        return res
