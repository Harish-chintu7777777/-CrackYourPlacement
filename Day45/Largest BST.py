
class Result:
    def __init__(self, size, min_val, max_val):
        self.size = size
        self.min = min_val
        self.max = max_val

class Solution:
    
    def solve(self, root):
        if not root:
            return Result(0, sys.maxsize, -sys.maxsize)
        
        left = self.solve(root.left)
        right = self.solve(root.right)
        
        if root.data > left.max and root.data < right.min:
            return Result(
                1 + left.size + right.size,
                min(root.data, left.min),
                max(root.data, right.max)
            )
        
        return Result(max(left.size, right.size), -sys.maxsize, sys.maxsize)
    
    def largestBst(self, root):
        return self.solve(root).size
