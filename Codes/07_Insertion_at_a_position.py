# A Node is one element of the linked list.
# Every node stores:
# 1. data = the actual value
# 2. next = reference to the next node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# ---------------------------------------------------------
# INSERT AT THE BEGINNING
# ---------------------------------------------------------
def insert_at_the_beginning(head, value):

    # Create a new node containing the given value.
    new_node1 = Node(value)

    # The new node should point to the OLD head.
    #
    # Before:
    # head
    #  ↓
    # 20 -> 30 -> 40
    #
    # After this line:
    # 10 -> 20 -> 30 -> 40
    new_node1.next = head

    # Now make the new node the new head.
    head = new_node1

    # Return the new head because head has changed.
    return head


# ---------------------------------------------------------
# INSERT AT THE END
# ---------------------------------------------------------
def insert_at_the_end(head, value):

    # Create the node that we want to add.
    new_node2 = Node(value)

    # SPECIAL CASE:
    # If the list is empty, there is no node to traverse.
    # Therefore the new node itself becomes the head.
    if head is None:
        head = new_node2
        return head

    # Start traversal from the first node.
    current = head

    # Keep moving until current reaches the LAST node.
    #
    # We check current.next because:
    # Last node's next is None.
    while current.next:
        current = current.next

    # current is now the last node.
    # Connect the last node to our new node.
    current.next = new_node2

    # The original head did not change,
    # but return it because we use:
    # head = insert_at_the_end(...)
    return head


# ---------------------------------------------------------
# INSERT AT A SPECIFIC POSITION
# ---------------------------------------------------------
def insert_at_a_position(head, value, position):

    # Create the node that we want to insert.
    middle_node = Node(value)

    # SPECIAL CASE:
    # Position 0 means insertion at the beginning.
    #
    # First connect the new node to the old head.
    # Then make the new node the new head.
    if position == 0:
        middle_node.next = head
        head = middle_node
        return head

    # Start traversal from head.
    # index keeps track of the position of current.
    current = head
    index = 0

    # To insert at position P,
    # current must stop at position P - 1.
    #
    # Example:
    #
    # index:   0     1     2
    #         10 -> 20 -> 40
    #
    # To insert 30 at position 2,
    # current should stop at index 1 (node 20).
    #
    # current.next is not None protects us from
    # moving beyond the end of the linked list.
    while index < position - 1 and current.next is not None:
        current = current.next
        index += 1

    # If we couldn't reach position - 1,
    # the requested position is outside the list.
    if index != position - 1:
        print("Invalid position")

        # Return the ORIGINAL head.
        # We should NOT return the error message because:
        #
        # head = insert_at_a_position(...)
        #
        # stores whatever the function returns inside head.
        return head

    # current is now ONE node before
    # where the new node should be inserted.
    #
    # Example:
    #
    # 20 -> 40
    #
    # First:
    # 30 -> 40
    middle_node.next = current.next

    # Then:
    # 20 -> 30 -> 40
    current.next = middle_node

    # Return the head of the linked list.
    return head


# ---------------------------------------------------------
# CREATE / BUILD THE LINKED LIST
# ---------------------------------------------------------

# Initially the linked list is empty.
head = None

# Add 50.
# Since the list is empty, 50 becomes the head.
head = insert_at_the_end(head, 50)

# Insert 40 before 50.
head = insert_at_the_beginning(head, 40)

# Add 60 at the end.
head = insert_at_the_end(head, 60)

# Insert 30 at the beginning.
head = insert_at_the_beginning(head, 30)

# Add 70 at the end.
head = insert_at_the_end(head, 70)

# Insert 20 at the beginning.
head = insert_at_the_beginning(head, 20)

# Try inserting 45 at a specific position.
head = insert_at_a_position(head, 45, 3)


# ---------------------------------------------------------
# TRAVERSAL / PRINT THE LINKED LIST
# ---------------------------------------------------------

# Start from the head.
current = head

# Keep going until current becomes None.
while current:

    # Print the value stored in the current node.
    print(current.data)

    # Move to the next node.
    current = current.next