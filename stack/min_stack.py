class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class MinStack:

    def __init__(self):
        self.length = 0
        self.head = None

    def push(self, val: int) -> None:
        node = Node(val)
        self.length += 1
        if not self.head:
            self.head = node
            return
    
        node.next = self.head
        self.head = node

    def pop(self) -> None:
        node = self.head
        self.head = node.next
        return

    def top(self) -> int:
        return self.head.val
        
    def getMin(self) -> int:
        min_val = float('inf')
        node = self.head
        while node:
            if node.val < min_val:
                min_val = node.val
            node = node.next
        return min_val