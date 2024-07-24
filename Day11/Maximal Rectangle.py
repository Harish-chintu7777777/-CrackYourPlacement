Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
... class Solution:
...     def maxArea(self,mat,m,n):
...         # code here
...         def hist(arr):
...             n = len(arr)
...             right = [n for _ in range(n)]
...             left = [-1 for  _ in range(n)]
...             stk = [n-1]
...             for i in range(n-2,-1,-1):
...                 while(stk and arr[i] <= arr[stk[-1]]):
...                     stk.pop()
...                 if stk:
...                     right[i] = stk[-1]
...                 stk.append(i)
...             stk = [0]
...             for i in range(1,n):
...                 while(stk and arr[i] <= arr[stk[-1]]):
...                     stk.pop()
...                 if stk:
...                     left[i]=stk[-1]
...                 stk.append(i)
...             maxi = -1e9
...             for i in range(n):
...                 maxi = max(maxi,(abs(left[i]-right[i])-1)*arr[i])
...             return maxi                
...         maxi = -1e9
...         hei = [0]*n
...         for i in range(m):
...             
...             for j in range(n):
...                 if mat[i][j] == 1:
...                     hei[j] += 1
...                 else:
...                     hei[j] = 0
...             maxi = max(maxi,hist(hei))
...             
