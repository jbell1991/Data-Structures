"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev # points to None by default
        self.next = next # points to None by default

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next # points to self.next which is None by default
        self.next = ListNode(value, self, current_next) # self.next points at a new ListNode we created
        if current_next: # checking if current_next is a node or none
            current_next.prev = self.next # current_next previous is node that comes before it

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev: # if prev is not None
            self.prev.next = self.next # look at the previous items next and move the next to the item after self
        if self.next: # if next is not None
            self.next.prev = self.prev # take the next item and move the prev pointer to the item before self


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None): 
        self.head = node # head pointer that is on None
        self.tail = node # tail pointer that is on None
        self.length = 1 if node is not None else 0 # length is 1 if node is not None otherwise length is 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # create a new_node
        new_node = ListNode(value, None, None)
        # check if the doubly-linked-list is empty:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        removed_node = self.head
        if self.head is None:
            return None
        else:
            self.head.delete()
            self.head = removed_node.next
            self.tail = None
            self.length -= 1
        return removed_node.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        removed_node = self.tail
        if self.tail is None:
            return None
        else:
            self.tail.delete()
            self.tail = removed_node.prev
            self.head = None
            self.length -= 1
        return removed_node.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return node
        else:
            self.add_to_head(node.value)
            self.delete(node)
        
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return node
        else:
            self.add_to_tail(node.value)
            self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        max = 0
        node = self.head
        while node:
            if node.value > max:
                max = node.value
            node = node.next
        return max
