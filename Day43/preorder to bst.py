# class Node:

#     def __init__(self, data=0):
#         self.data = data
#         self.left = None
#         self.right = None

#Function that constructs BST from its preorder traversal.
def insertBST(root,data):
    if root is None:
        return Node(data)
    elif root.data<data:
        root.right=insertBST(root.right,data)
    else:
        root.left=insertBST(root.left,data)
    return root
    
def post_order(pre, size) -> Node:
    root=None
    for i in range(size):
        root=insertBST(root,pre[i])
    return root
