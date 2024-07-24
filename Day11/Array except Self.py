
class Solution:
    def productExceptSelf(self, nums, n):
        n = len(nums)
        if n == 1:
            return [1]
        pre = [1] * n
        suff = [1] * n
    
        pre[0] = nums[0]
        suff[n - 1] = nums[-1]
    
        for i in range(1, n):
            pre[i] = nums[i] * pre[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i] * suff[i + 1]
    
        result = [1] * n
        for i in range(n):
            if i == 0:
                result[i] = suff[i + 1]
            elif i == n - 1:
                result[i] = pre[i - 1]
            else:
                result[i] = pre[i - 1] * suff[i + 1]
    
        return result
class Solution:
    def productExceptSelf(self, nums, n):
        n = len(nums)
        if n == 1:
            return [1]
        pre = [1] * n
        suff = [1] * n
    
        pre[0] = nums[0]
        suff[n - 1] = nums[-1]
    
        for i in range(1, n):
            pre[i] = nums[i] * pre[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i] * suff[i + 1]
    
        result = [1] * n
        for i in range(n):
            if i == 0:
                result[i] = suff[i + 1]
            elif i == n - 1:
                result[i] = pre[i - 1]
            else:
                result[i] = pre[i - 1] * suff[i + 1]
    
        return result
