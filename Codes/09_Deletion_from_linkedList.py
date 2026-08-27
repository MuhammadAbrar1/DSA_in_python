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
    current = head
    while current.next:
        current=current.next
    current.next=new_node2
    return head
def insert_at_a_position(head,value,position):
    middle_node=Node(value)
    if position == 0:
        middle_node.next=head
        head =middle_node
        return head
    current=head
    index=0
    while index<position-1 and current.next is not None:
        current=current.next
        index+=1
    if index!=position-1:
        print("Invalid position")
        return head
    middle_node.next=current.next
    current.next=middle_node
    return head
def delete_from_the_beginning(head):
    if head is None:
        print("LinkedList is empty")
        return head
    head = head.next
    return head
def delete_from_the_end(head):
    if head is None:
        print("LinkedList is empty")
        return head
    current=head
    if head.next is None:
        head = None
        return head
    while current.next.next:
        current=current.next
    current.next=None
    return head
def delete_from_a_position(head,position):
    if head is None:
            print("LinkedList is empty")
            return head
    if position==0:
        head=head.next
        return head
    current=head
    index=0
    while index<position-1 and current.next is not None:
        current=current.next
        index+=1
    if index!=position-1:
        print("Invalid position")
        return head
    if current.next is None:
        print(f"Position {position} is invalid")
        return head
    current.next=current.next.next
    return head

head = None
head=insert_at_the_end(head,50)
head=insert_at_the_beginning(head,40)
head=insert_at_the_end(head,60)
head=insert_at_the_beginning(head,30)
head=insert_at_the_end(head,70)
head=insert_at_the_beginning(head,20)
head=insert_at_a_position(head,45,3)
head=insert_at_a_position(head,55,100)
head=delete_from_the_beginning(head)
head=delete_from_the_end(head)
head=delete_from_a_position(head,2)
current=head
while current:
    print(current.data)
    current=current.next