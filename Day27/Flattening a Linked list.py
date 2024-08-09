

'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(root):
    #Your code here
    l=[]
    curr=root
    while(curr):
        curr1=curr
        while(curr1 is not None):
            l.append(curr1.data)
            curr1=curr1.bottom
        curr=curr.next
    l.sort()
    dummy=Node(-1)
    ind=dummy
    for i in l:
        dummy.bottom=Node(i)
        dummy=dummy.bottom
    return ind.bottom
