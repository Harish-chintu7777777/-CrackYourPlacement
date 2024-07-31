class Solution:

    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        #Code here
        arr=grid
        que=[]
        l=len(arr[0])
        for i in range(len(arr)):
              for j in range(l):
                  if arr[i][j]==2:
                     que.append([i,j,0])
                  else :
                      continue
        t=0
        while que:
              i,j,t=que.pop(0)
              for r,c in [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]:
                         if 0<=r<len(arr) and 0<=c<l and arr[r][c]==1:
                               arr[r][c]=2
                               que.append([r,c,t+1])
        return -1 if any(c == 1 for r in arr for c in r) else t
               
                
            
                    
         
         
        
