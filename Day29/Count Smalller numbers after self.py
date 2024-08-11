Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class Solution:
...     def countSmaller(self, nums: List[int]) -> List[int]:  
... 
...         def merge(left, right, res):
...             i, j, m, n = 0, 0, len(left), len(right)
...             result = []
...             while i < m and j < n:
...                 if left[i][1] > right[j][1]:
...                     res[left[i][0]] += n - j
...                     result.append(left[i])
...                     i += 1
...                 else:
...                     result.append(right[j])
...                     j += 1
...             result.extend(left[i:])
...             result.extend(right[j:])
...             return result
... 
...         def divide(nums, res):
...             if len(nums) <= 1:
...                 return nums
...             mid = len(nums) // 2
...             left = divide(nums[:mid], res)
...             right = divide(nums[mid:], res)
...             return merge(left, right, res)
... 
...         res = [0] * len(nums)
...         nums_with_indices = [(i, nums[i]) for i in range(len(nums))]
...         divide(nums_with_indices, res)
...         return res
