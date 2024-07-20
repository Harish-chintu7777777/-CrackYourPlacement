Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... 
... from collections import deque
... 
... class Solution:
...     def fill(self, n, m, mat):
...         q=deque()
...         lis1=[-1,1,0,0]
...         lis2=[0,0,-1,1]
...         for i in range(n):
...             for j in range(m):
...                 if i==0 or j==0 or i==n-1 or j==m-1:
...                     if mat[i][j]=='O':
...                         q.append([i,j])
...                         mat[i][j]='q'
...         
...         while q:
...             t=q.popleft()
...             r=t[0]
...             c=t[1]
...             
...             for i in range(4):
...                 nr=r+lis1[i]
...                 nc=c+lis2[i]
...                 
...                 if nr>=0 and nc>=0 and nr<n and nc<m and mat[nr][nc]=='O':
...                     q.append([nr,nc])
...                     mat[nr][nc]="q"
...         for i in range(n):
...             for j in range(m):
...                 if mat[i][j]=='O':
...                     mat[i][j]='X'
...                 if mat[i][j]=='q':
...                     mat[i][j]='O'
...         return mat
...     
...             
...         
