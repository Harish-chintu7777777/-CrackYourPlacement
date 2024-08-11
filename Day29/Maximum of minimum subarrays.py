class Solution:
    def maxOfMin(self,arr,n):
        left = [-1] * n 
        right = [n] * n  
        stack = []
    
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
    
        stack = []
        
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        result = [0] * (n + 1)
       
        for i in range(n):
            
            window_size = right[i] - left[i] - 1
            result[window_size] = max(result[window_size], arr[i])
       
        for i in range(n-1, 0, -1):
            result[i] = max(result[i], result[i+1])
        return result[1:]
