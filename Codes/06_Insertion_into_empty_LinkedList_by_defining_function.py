class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next

# head=None
# first_node=Node(10)
# first_node.next=head
# head=first_node
# current = head
# while current:
#     print(current.data)
#     current=current.next


def insert_at_the_beginning(head,value):
    new_node=Node(value)
    new_node.next=head
    head=new_node
    return head
head=None
head = insert_at_the_beginning(head,20)
Current=head
while Current:
    print(Current.data)
    Current=Current.next
