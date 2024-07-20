import sys
sys.setrecursionlimit(10**8)
class Solution:
    def traverse(self,grid,row,col):
        self.visited[row][col]=1
        for i,j in self.moves:
            if 0<=i+row<self.rows and 0<=j+col<self.cols and grid[i+row][j+col]==1 and self.visited[i+row][j+col]==0:
                self.traverse(grid,i+row,j+col)
    def numIslands(self,grid):
        #code here
        self.moves=[[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]
        self.rows=len(grid)
        self.cols=len(grid[0])
        self.visited=[[0 for i in range(self.cols)]for i in range(self.rows)]
        res=0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j]==1 and self.visited[i][j]==0:
                    self.traverse(grid,i,j)
                    res+=1

        return res
