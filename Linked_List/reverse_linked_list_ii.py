from typing import Optional;
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int, idx = 1, prev = None) -> Optional[ListNode]:
        if (idx >= right): return head;
        
        if (idx < left):
            idx += 1
            return self.reverseBetween(head.next, left, right, idx);
        
        temp = head.next;
        head.next = prev;
        prev = head;
        head = temp;
        idx += 1;
        return self.reverseBetween(head, left, right, idx, prev);