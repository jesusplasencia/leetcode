from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 48 ms
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while (fast and fast.next):
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast): return True;
        return False;

    # 53 ms 
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = set();
        current = head;
        while (current):
            if (current not in d):
                d.add(current);
            else:
                return True;
            current = current.next;
        return False;

Head = ListNode(3); 
A = ListNode(2);
B = ListNode(0);
C = ListNode(4);
Head.next = A;
A.next = B;
B.next = C;
C.next = B; 
print(Solution().hasCycle(Head));