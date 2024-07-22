class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        z,o,t = 0,0,0
        curr = head
        while(curr):
            if curr.data==0:
                z+=1
            elif curr.data==1:
                o+=1
            else:
                t+=1
            curr = curr.next
        curr = head
        while(z):
            curr.data=0
            z-=1
            curr = curr.next
        while(o):
            curr.data = 1
            o-=1
            curr = curr.next
        while(t):
            curr.data = 2
            t-=1
            curr = curr.next
        return head
