#User function Template for python3

def findMedian(root):
    # code here
    # return the median
    l=[]
    def f(root):
        if not root: return
        f(root.left)
        l.append(root.data)
        f(root.right)
    f(root)
    n=len(l)
    if len(l)%2==0:
        m=(l[n//2]+l[n//2-1])/2
        if int(m)==m:
            return int(m)
        return m
    return l[n//2]

