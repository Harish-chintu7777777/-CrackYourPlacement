class Solution:

    #Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, kpos, tpos, n):
        #Code here
        vis=set()
        for i in range(1,n+1):
            for j in range(1,n+1):
                if kpos[0]==i and kpos[1]==j:
                    
                    q=[]
                    steps=0
                    q.append((i,j,steps))
                    vis.add((i,j))
                    while(q):
                        row,col,c=q.pop(0)
                        if row==tpos[0] and col==tpos[1]:
                            return c
                        else:
                            for r,c1 in [[-1,2],[-1,-2],[1,2],[1,-2],[-2,-1],[-2,1],[2,-1],[2,1]]:
                                nrow=r+row
                                ncol=c1+col
                                if 1<=nrow<(n+1) and 1<=ncol<(n+1) and (nrow,ncol) not in vis:
                                    q.append((nrow,ncol,c+1))
                                    vis.add((nrow,ncol))
        
        
                    
