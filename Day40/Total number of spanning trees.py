class Solution:
    def countSpanningTrees(self, graph : List[List[int]],m : int,n : int) -> int:
        M = np.zeros(shape=(m, m))
        indegree = [0 for _ in range(m)]
        
        for edge in graph:
            u,v = edge
            M[u,v] = -1
            M[v,u] = -1
            indegree[u] += 1
            indegree[v] += 1
        
        for i in range(m):
            M[i,i] = indegree[i]
        
        noOfSpanningTrees = np.linalg.det(M[1:, 1:])
        
        return int(round(noOfSpanningTrees))
