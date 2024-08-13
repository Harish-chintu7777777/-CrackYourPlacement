# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        @cache
        def f(start,end):
            if start>end:
                return [None]
            if start==end:
                return [TreeNode(start)]
            ans = []
            for i in range(start,end+1):
                left = f(start,i-1)
                right = f(i+1,end)
                for l in left:
                    for r in right:
                        ans.append(TreeNode(i,l,r))
            return ans
        return f(1,n)
