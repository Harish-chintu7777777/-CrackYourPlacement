# Your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isDeadEnd(self, root):
        # Code here
        # vis = set()
        # def f(root):
        #     if not root:
        #         return 
        #     f(root.left)
        #     vis.add(root.data)
        #     f(root.right)
        # def f1(root):
            
        #     if not root.left and not root.right and root.data-1 in vis and root.data+1 in vis:
        #         return True
        #     f1(root.left)
        #     f1(root.right)
        #     return False
        # f(root)
        # x = f1(root)
        # if x:
        #     return 1
        # return 0
        

        if root == None:
            return False

        all = set()
        leaves = set()
        q = []
        q.append(root)
        while(q):
            curr = q.pop(0)
    
            # Insert the data of all the nodes to the "all" set.
            all.add(curr.data)
    
            # If the current node is a leaf node, then insert the data to the "leaves" set.
            if curr.left == None and curr.right == None:
                leaves.add(curr.data)
            else:
                if curr.left != None:
                    q.append(curr.left)
                if curr.right !=None:
                    q.append(curr.right)
    
        for data in leaves:
            if data == 1:
                if 2 in all:
                    return True
            elif (data - 1) in all:
                    if (data + 1) in all:
                        return True
    
        return False
