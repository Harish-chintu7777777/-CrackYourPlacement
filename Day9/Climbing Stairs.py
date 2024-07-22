Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class Solution:
...     def climbStairs(self, n: int) -> int:
...         # def f(ind,dp):
...         #     if ind<=2:
...         #         return ind
...         #     if dp[ind]!=-1:
...         #         return dp[ind]
...             
...         #     dp[ind]=f(ind-1,dp)+f(ind-2,dp)
...         #     return dp[ind]
... 
...         # dp=[-1 for i in range(n+1)]
...         # return f(n,dp)
... 
...         # dp=[-1 for i in range(n+1)]
...         # if n<=2: return n
...         # dp[0]=0
...         # dp[1]=1
...         # dp[2]=2
...         # for j in range(3,n+1):
...         #     dp[j]=dp[j-1]+dp[j-2]
...         # return dp[n]
... 
...         prev2,prev=0,1
...         for i in range(1,n+1):
...             cur=prev2+prev
...             prev2=prev
...             prev=cur
