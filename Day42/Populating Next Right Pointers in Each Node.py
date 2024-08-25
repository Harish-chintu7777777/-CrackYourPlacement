"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q=[root]
        while q:
            nxt=None
            for i in range(len(q)):
                node=q.pop(0)
                if nxt:
                    nxt.next=node
              
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 
                nxt=node
            
        return root

        




        
