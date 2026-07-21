class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
n1=Node(10)
n2=Node(15)
n3=Node(20)
n4=Node(25)
n1.next=n2
n2.next=n3
n3.next=n4
new_node=Node(5)
new_node.next=n1
n1=new_node
current=n1
while current:
    print(current.data)
    current=current.next

print()


# Drill 1 (Insert another value, 2, at the beginning of the current list)

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
n1=Node(10)
n2=Node(15)
n3=Node(20)
n4=Node(25)
new_node=Node(5)
second_new_node=Node(2)

n1.next=n2
n2.next=n3
n3.next=n4
new_node.next=n1
second_new_node.next=new_node
new_node=second_new_node
n1=new_node
current=n1
while current:
    print(current.data)
    current=current.next

print()


# Drill 2__insertion into an empty list.

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
head=None
first_node=Node(50)
first_node.next=head
head=first_node
current=head

while current:
    print(current.data)
    current=current.next

print()



# Drill 3__insertion into the end of a Linked List.

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
n1=Node(4)
n2=Node(8)
n3=Node(16)
n4=Node(32)
new_node=Node(64)

n1.next=n2
n2.next=n3
n3.next=n4

current=n1

while current.next:
    print(current.data)
    current=current.next
current.next=new_node
print()
while current:
    print(current.data)
    current=current.next


    """
while current:
    Checks whether current points to a real node.
    It processes the last node and then moves current to None.
    Therefore, it stops AFTER the last node.

while current.next:
    Checks whether another node exists after the current node.
    When current reaches the last node, current.next is None.
    Therefore, it stops ON the last node.

Use:
- while current      → for printing, counting, or visiting every node.
- while current.next → when you need to modify or connect something to the last node.
""" 