from typing import List

class Solution:
    def findPath(self, mat: List[List[int]]) -> List[str]:
        # code here
        def f(i,j,curr,vis):
            
            if i == n-1 and j == n-1:
                l.append(curr)
                return 
            vis.add((i,j))
             
            if i+1 < n and mat[i+1][j] == 1 and (i+1,j) not in vis:
                f(i+1,j,curr + 'D',vis)
                
            if i - 1 >= 0 and mat[i-1][j] == 1 and (i-1,j) not in vis:
                f(i-1,j,curr + 'U',vis)
                
            if j + 1 < n and mat[i][j+1] == 1 and (i,j+1) not in vis:
                f(i,j+1,curr + 'R',vis)
                
            if j-1 >= 0 and mat[i][j-1] == 1 and (i,j-1) not in vis:
                f(i,j-1,curr + 'L',vis)
            
            vis.remove((i,j))
            return
            
        n = len(mat)
        l, vis = [], set()
        if mat[0][0] == 0:
            return []
        f(0,0,"",vis)
        return l


