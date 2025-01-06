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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = [];
        current = head;
        while current:
            nums.append(current.val);
            current = current.next;

        dummy = ListNode(0);
        current = dummy;
        c = Counter(nums);
        for x in c:
            key = x;
            val = c[key];
            if (val > 1): continue;
            current.next = ListNode(x);
            current = current.next;
        return dummy.next;


if __name__ == "__main__":
    sol = Solution();
    print(sol.deleteDuplicates(ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))))