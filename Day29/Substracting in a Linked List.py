class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        
        s1, s2 = "", ""
        curr1, curr2 = l1, l2
        while(curr1):
            s1 += str(curr1.data)
            curr1 = curr1.next
        while(curr2):
            s2 += str(curr2.data)
            curr2 = curr2.next
        value = abs(int(s1) - int(s2))
        dummy = Node(-1)
        curr = dummy
        
        for i in str(value):
            curr.next = Node(int(i))
            curr = curr.next
        return dummy.next
