class Solution:
	def minSteps(self, m, n, d):
		
		q = [(0,0,0)]
		vis = {(0,0,0)}
		total = m+n
		while(q):
		    a, b , cnt = q.pop(0)
		    if a == d or b == d:
		        return cnt
		    for i,j in [(m,b),
		                (a,n),
		                (0,b),
		                (a,0),
		                (a - min(a,n-b), b+min(a,n-b)),
		                (a+min(b,m-a), b-min(b,m-a))]:
		        
		        if (i,j) not in vis:
		            vis.add((i,j))
		            q.append((i,j,cnt+1))
	    return -1
