# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def f(root, curr_sum):
            if not root:
                return

            curr_sum += root.val

            if curr_sum - targetSum in d:
                cnt[0] += d[curr_sum - targetSum]

            if curr_sum in d:
                d[curr_sum] += 1
            else:
                d[curr_sum] = 1

            f(root.left, curr_sum)
            f(root.right, curr_sum)

            d[curr_sum] -= 1

        cnt = [0]  
        d = {0: 1}  
        f(root, 0)
        return cnt[0]
