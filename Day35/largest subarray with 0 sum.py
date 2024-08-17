class Solution:
    def maxLen(self, n, arr):
        #Code here
        d={0:0}
        s=0
        c=0
        for i in range(len(arr)):
            s=s+arr[i]
            if s==0:
                c=i+1
            
            if s not in d:
                d[s]=i
                
            else:
                c=max(c,i-d[s])
        return c
