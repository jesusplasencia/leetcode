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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversed = self.reverse(head);
        dummy = ListNode(0, reversed);
        current = dummy;
        idx = 0;
        while (current and current.next):
            if (idx + 1 == n):
                current.next = current.next.next;
            current = current.next;
            idx += 1;
        return self.reverse(dummy.next);

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None;
        current = head;

        while (current):
            tmp = current.next;
            current.next = prev;
            prev = current;
            current = tmp;

        return prev;

if __name__ == "__main__":
    sol = Solution();
    print(sol.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2));