class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
def insert_at_the_beginning(head,value):
    new_node1=Node(value)
    new_node1.next=head
    head=new_node1
    return head
def insert_at_the_end(head,value):
    new_node2=Node(value)
    if head is None:
        head = new_node2
        return head
    current=head
    while current.next:
        current=current.next
    current.next=new_node2
    return head
def insert_at_a_position(head,value,position):
    middle_node=Node(value)
    if position==0:
        middle_node.next=head
        head = middle_node
        return head
    current = head
    index=0
    while index<position-1 and current.next is not None:
        current=current.next
        index+=1
    if index!=position-1:
        print("Invalid Position")
        return head
    middle_node.next=current.next
    current.next=middle_node
    return head
head = None
head=insert_at_the_end(head,50)
head=insert_at_the_beginning(head,40)
head=insert_at_the_end(head,60)
head=insert_at_the_beginning(head,30)
head=insert_at_the_end(head,70)
head=insert_at_the_beginning(head,20)
head=insert_at_a_position(head,45,3)
current=head
while current:
    print(current.data)
    current=current.next