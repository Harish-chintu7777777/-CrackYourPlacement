def zigzag(self, head):

        if head:
            temp=head
            c=0
            while temp.next:
                if c%2==0:
                    if temp.data>temp.next.data:
                        a=temp.data
                        temp.data=temp.next.data
                        temp.next.data=a
                else:
                    if temp.data<temp.next.data:
                        a=temp.data
                        temp.data=temp.next.data
                        temp.next.data=a
                c+=1
                temp=temp.next
            return head
