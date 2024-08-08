'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        
        
        
        mod=10**9+7
        n1,n2=0,0
        while head1:
            n1=n1*10+head1.data
            head1=head1.next
        while head2:
            n2=n2*10+head2.data
            head2=head2.next
        return (n1*n2)%mod
