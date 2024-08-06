class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        mat = [[1e9]*n for _ in range(n)]
        for i,j,k in edges:
            mat[i][j] = k
            mat[j][i] = k
        for i in range(n):
            mat[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i!=j:
                        mat[i][j] = min(mat[i][j],mat[i][k] + mat[k][j])
        mini = 1e9
        city = -1
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i!=j and mat[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt < mini or (cnt == mini and i > city):
                city = i
                mini = cnt
        return city
