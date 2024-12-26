from typing import Optional;
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val;
        self.next = next;

    def toArray(self):
        res = [];
        while (self):
            res.append(str(self.val));
            self = self.next;
        return res;

    def __str__(self):
        return ' -> '.join(self.toArray());
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:        
        dummy = ListNode(0, head);
        leftPrev, curr = dummy, head
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next
        
        prev = None;
        for j in range(right - left + 1):
            temp = curr.next;
            curr.next = prev
            prev, curr = curr, temp

        leftPrev.next.next = curr;
        leftPrev.next = prev;
        return dummy.next;