Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>       class Solution:
... 	def shortest_distance(self, matrix):
... 		#Code here
... 		m=len(matrix)
... 		
... 		for i in range(m):
... 		    for j in range(m):
... 		        if matrix[i][j]==-1:
... 		            matrix[i][j]=float('inf')
... 		for k in range(m):
... 		    for i in range(m):
... 		        for j in range(m):
... 		            matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
... 		for i in range(m):
... 		    for j in range(m):
... 		        if matrix[i][j]==float('inf'):
... 		            matrix[i][j]=-1
