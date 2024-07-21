class Solution:
    def missingNumber(self,arr,n):
        #Your code here
        s=set(arr)
        i=1
        while(i in s):
            i+=1
        return i
