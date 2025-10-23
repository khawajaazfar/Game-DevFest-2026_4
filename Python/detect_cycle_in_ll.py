class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def create_cycle(self, pos):
        """Create a cycle in the linked list at the given position (0-indexed)."""
        if pos == -1:
            return 
        cycle_node = None
        temp = self.head
        index = 0
        last = None
        while temp:
            if index == pos:
                cycle_node = temp
            last = temp
            temp = temp.next
            index += 1
        if last and cycle_node:
            last.next = cycle_node 

def is_cycle_found(head):
    """Detects if a cycle exists in the linked list using Floyd's cycle-finding algorithm."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 5, -4]:
        ll.append(val)

    # Uncomment the next line if you want to create a cycle at index 1
    ll.create_cycle(1)

    if is_cycle_found(ll.head):
        print("Cycle detected")
    else:
        print("No cycle detected")
