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
