class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Create one node
n1 = Node(10)          # data = 10, next = None

print(n1.data)         # 10
print(n1.next)         # None

# One node exists, but it is not linked to another node yet.

"""so far nothing magical happened"""




class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Create two separate nodes
n2 = Node(5)           # data = 5, next = None
n3 = Node(15)          # data = 15, next = None

print(n2.data)         # 5
print(n3.data)         # 15

# Both nodes are independent because neither node points to the other.

"""these are completely independent. there is still no lnked list yet"""



## FIRST LINK

# A node stores two things:
# 1. Its own data
# 2. A reference to the next node

class Node:
    def __init__(self, data=None, next=None):
        self.data = data      # Value stored inside this node
        self.next = next      # Reference to the next node


# Create two separate nodes
n4 = Node(32)
n5 = Node(12)

# Link n4 with n5:
# 32 -> 12 -> None
n4.next = n5

# Print the data of the current node
print(n4.data)          # 32

# Go to the next node and print its data
print(n4.next.data)     # 12



# THREE NODES

# Create three separate nodes
n6 = Node(100)      # data = 100, next = None
n7 = Node(46)       # data = 46, next = None
n8 = Node(19)       # data = 19, next = None

# Link the nodes together
n6.next = n7        # 100 -> 46
n7.next = n8        # 46 -> 19

# Current linked list:
# 100 -> 46 -> 19 -> None

print(n6.data)              # 100
print(n6.next.data)         # 46 (move one node forward)
print(n6.next.next.data)    # 19 (move two nodes forward)


# Every ".next" moves one node forward.
#
# n6.data            -> 100
# n6.next.data       -> 46
# n6.next.next.data  -> 19



