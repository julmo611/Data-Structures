"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
        return self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
        return self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.length > 0:
            old_head = self.head
            new_head = old_head.insert_before(value)
            self.head = new_head
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1

    def remove_from_head(self):
        if self.length > 0:
            old_head = self.head
            new_head = None
            if self.head.next:
                new_head = self.head.next
            if self.tail is old_head:
                self.tail = None

            old_head.delete()
            self.head = new_head
            self.length -= 1
            return old_head.value

    def add_to_tail(self, value):
        if self.length > 0:
            old_tail = self.tail
            new_tail = old_tail.insert_after(value)
            self.tail = new_tail
        else:
            self.tail = ListNode(value)
            self.head = self.tail
        self.length += 1

    def remove_from_tail(self):
        if self.length > 0:
            old_tail = self.tail
            new_tail = None
            if self.tail.next:
                new_tail = self.tail.next
            if self.head is old_tail:
                self.head = None

            old_tail.delete()
            self.tail = new_tail
            self.length -= 1
            return old_tail.value

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    def delete(self, node):
        if self.length > 0:
            old_next = node.next
            old_prev = node.prev

        if old_next:
            old_next.prev = old_prev
        if old_prev:
            old_prev.next = old_next

        if self.tail is node:
            self.tail = node.prev
        if self.head is node:
            self.head = node.next

        node.delete()
        self.length -= 1

    def get_max(self):
        current = self.head
        max_value = current.value
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value
