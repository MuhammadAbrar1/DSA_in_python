# Insertion at the beginning.


class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next

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
print()




# Drill 1

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
def insert_at_the_beginning2(head,value):
    new_node1=Node(value)
    new_node1.next=head
    head=new_node1
    return head
head = None
Current=head
head=insert_at_the_beginning2(head,20)
head=insert_at_the_beginning2(head,30)
head=insert_at_the_beginning2(head,40)
Current=head
while Current:
    print(Current.data)
    Current=Current.next
print() 


# Drill 2

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
def insert_at_the_beginning3(head,value):
    new_node2=Node(value)
    new_node2.next=head
    head=new_node2
    return head
head=None
head=insert_at_the_beginning3(head,50)
head=insert_at_the_beginning3(head,10)
head=insert_at_the_beginning3(head,80)
head=insert_at_the_beginning3(head,30)
Current=head
while Current:
    print(Current.data)
    Current=Current.next
print()




# Insertion at the End.

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
def insert_at_the_end(head,value):
    new_node=Node(value)
    if head==None:
        head=new_node
        return head
    current=head
    while current.next:
        current=current.next
    current.next=new_node
    return head
head=None
head=insert_at_the_end(head,2)
head=insert_at_the_end(head,4)
head=insert_at_the_end(head,6)
head=insert_at_the_end(head,8)
head=insert_at_the_end(head,10)
head=insert_at_the_end(head,12)
head=insert_at_the_end(head,14)
head=insert_at_the_end(head,16)

current=head
while current:
    print(current.data)
    current=current.next



class Node:
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=next

def insert_at_the_beginning(head,value):
    new_node1=Node(value)
    new_node1.next=head
    head = new_node1
    return head
def insert_at_the_end(head,value):
    new_node=Node(value)
    if head is None:
        head = new_node
        return head
    current = head
    while current.next:
        current=current.next
    current.next=new_node
    return head

head = None
head = insert_at_the_end(head,20)
head = insert_at_the_beginning(head,10)
head = insert_at_the_end(head,30)
head = insert_at_the_beginning(head,5)
current=head
while current:
    print(current.data)
    current=current.next