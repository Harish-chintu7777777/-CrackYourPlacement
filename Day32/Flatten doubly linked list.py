
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head
        while curr:
            if curr.child:
                temp = curr.child
                while temp.next:
                    temp = temp.next
                if curr.next:
                    curr.next.prev = temp
                temp.next = curr.next
                
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            curr = curr.next
        return head
