# Definition for singly-linked list.
from typing import Optional;
from collections import Counter;

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = [];
        while (self):
            result.append(str(self.val));
            self = self.next;
        return ' -> '.join(result);

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (k == 0): return head;
        current = self.rotate(head);
        for _ in range(k - 1):
            current = self.rotate(current);
        return current;

    def rotate(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # If the list is empty or has one node, no rotation is needed
            return head

        dummy = ListNode(0, head)
        current = head
        prev = None

        # Traverse to the end of the list
        while current.next:
            prev = current
            current = current.next

        # Rotate the list
        current.next = dummy.next  # Point the last node to the head
        dummy.next = current       # Update the new head
        prev.next = None           # Break the cycle by making the new tail point to None

        return dummy.next

if __name__ == "__main__":
    sol = Solution();
    print(sol.rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2));