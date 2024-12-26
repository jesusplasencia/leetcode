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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        cur = head;
        prev = None;

        while cur:
            temp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = temp;

        return prev;

if __name__ == "__main__":
    sol = Solution();
    print(sol.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))));