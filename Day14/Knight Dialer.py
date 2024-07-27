Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def knightDialer(self, n: int) -> int:
        mat = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
        m = len(mat)
        n1 = len(mat[0])
        # dp = [[-1] * n1 for _ in range(m)]
...         cache={}
...         pos = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
...         cnt = 0
...         mod=10**9+7
...         def isInvalid(r, c):
...             if r >= 4 or c >= 3 or r < 0 or c < 0:
...                 return True
...             if (r, c) in [(3, 0), (3, 2)]:
...                 return True
...             return False
...         def f(x, y, l):
...             if isInvalid(x,y): return 0
...             if l == n:
...                 return 1
...             
...             # if dp[x][y] != -1:
...             #     return dp[x][y]
...             if (x,y,l) in cache:
...                 return cache[(x,y,l)]
...             s=0
...             for i,j in pos:
...                 r=x+i
...                 c=y+j
...     
...                 s += f(r,c,l+1)
...             # dp[x][y] = s%mod
...             # return dp[x][y]
...             cache[(x,y,l)]=s
...             return cache[(x,y,l)]%mod
...             
...         for i in range(m):
...             for j in range(n1):
...                 if mat[i][j] != "*" and mat[i][j] != "#":
...                     cnt += f(i, j, 1)
... 
...         return cnt%mod
... 
...         
