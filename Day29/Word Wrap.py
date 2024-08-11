Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #User function Template for python3
... 
... class Solution:
... 	def solveWordWrap(self, nums, k):
... 		#Code here
... 		def f(curr, spaces):
... 		    
... 		    if curr == n:
... 		        return 0
... 		    if (curr, spaces) in dp:
... 		        return dp[(curr, spaces)]
... 		    new_spaces = spaces + 1 + nums[curr]
... 		    a = float('inf')
... 		    if new_spaces <= k:
... 		        a = f(curr + 1, new_spaces)
... 		    b = f(curr + 1, nums[curr]) + (k - spaces) * (k-spaces)
... 		    
... 		    dp[(curr, spaces)] = min(a,b)
... 		    return min(a, b)
... 		    
... 	    dp = {}
