#User function Template for python3

#User function Template for python3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


#Back-end complete function Template for Python 3
class Solution:
    
    def reorderList(self,head):
        if head.next==None:
            return head
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        l1=slow.next
        slow.next=None
        prev=None
        later=None
        while(l1):
            later=l1.next
            l1.next=prev
            prev=l1
            l1=later
        head1, head2 = head, prev
        while head1 and head2:
            nextt = head1.next
            head1.next = head2
            head1=head2
            head2=nextt
        return head1
