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
    if head.next is None:
        head.next = new_node2
        return head
    current=head
    while current.next:
        current=current.next
    current.next = new_node2
    return head
def insert_at_a_position(head,value,position):
    middle_node=Node(value)
    if position==0:
        middle_node.next=head
        head=middle_node
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
def search_for_a_value(head,value):
    current=head
    while current:
        if current.data==value:
            print(f"{value} is found")
            return head
        current=current.next
    print(f"{value} is not found")
    return head
def length_of_LinkedList(head):
    current=head
    length=0
    while current:
        length+=1
        current=current.next
    print(f"Length of LinkedList is {length}")
    return head
    


head=None
head=insert_at_the_end(head,50)
head=insert_at_the_beginning(head,40)
head=insert_at_the_end(head,60)
head=insert_at_the_beginning(head,30)
head=insert_at_the_end(head,70)
head=insert_at_the_beginning(head,20)
head=insert_at_a_position(head,45,3)
head=search_for_a_value(head,20)
head=length_of_LinkedList(head)
current=head
while current:
    print(current.data)
    current=current.next