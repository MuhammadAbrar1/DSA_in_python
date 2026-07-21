class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next
n1=Node(2)
n2=Node(4)
n3=Node(6)
n4=Node(8)
n5=Node(10)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
current=n1

# Traversal = Visit every node in the linked list.

# current starts from the first node.
current = n1

# Continue until there are no more nodes.
while current:

    # Process the current node.
    print(current.data)

    # Move to the next node.
    current = current.next


# drill 1 ,2(counting) and 3(Summation)

class Node1:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
n1=Node1(5)
n2=Node(10)
n3=Node(15)
n4=Node(20)
n5=Node(25)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
current=n1
count=0
summation=0
while current:
    print(current.data)
    count+=1
    summation=summation+current.data    
    current=current.next
print(count)
print(summation)