class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        def bfs(row,col):
            q=[]
            q.append((row,col))
            vis.add((row,col))
            while(q):
                r,c=q.pop(0)
                for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nrow=r+i
                    ncol=c+j
                    if (0<=nrow<m and 0<=ncol<n and (nrow,ncol) not in vis and grid[nrow][ncol]=="1"):
                        q.append((nrow,ncol))
                        bfs(nrow,ncol)
        
        
        
        c=0
        vis=set()
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in vis:
                    c+=1
                    bfs(i,j)
        
        
        return c


        
        


       
