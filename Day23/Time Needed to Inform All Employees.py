
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def f(node):
            if node not in d:
                return 0
            maxi = 0
            for it in d[node]:
                maxi = max(maxi, informTime[node] + f(it))
            return maxi
        
        d = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                d[manager[i]].append(i)
                
        return f(headID)
