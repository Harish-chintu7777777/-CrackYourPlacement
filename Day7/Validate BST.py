def validate(left,root,right):
    if not root:
        return True
    if not(left<root.val and right>root.val):
        return False
    return validate(left,root.left,root.val) and validate(root.val,root.right,right)
return validate(float("-inf"),root,float("inf"))
