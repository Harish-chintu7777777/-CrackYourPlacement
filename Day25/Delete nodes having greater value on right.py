#User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        #Your code here
        
        l = []
        curr = head
        while(curr):
            l.append(curr.data)
            curr = curr.next
        m = [l[-1]]
        for i in range(len(l)-2,-1,-1):
            if m[-1]<=l[i]:
                m.append(l[i])
        m = m[::-1]
        dummy = Node(-1)
        ss = dummy
        n=len(m)
        i = 0
        while(n>0):
            dummy.next = Node(m[i])
            dummy = dummy.next
            i+=1
            n-=1
        return ss.next

