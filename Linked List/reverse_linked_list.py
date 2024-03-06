# Given the head of a singly linked list, reverse the list, and return the reversed list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def print_linked_list(head):
    if not head:
        return
    if head:
        print(head.value, " -> " if head.next else "", end="")
    print_linked_list(head.next)


tail = Node(1)
tail.next = Node(4)
tail.next.next = Node(7)
tail.next.next.next = Node(8)

reversed_linked_list = reverse_linked_list(tail)
print_linked_list(reversed_linked_list)




