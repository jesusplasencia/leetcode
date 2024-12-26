from typing import Optional;
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: Optional[int] = 0) -> Optional[ListNode]:
        if (not l1 and not l2 and carry == 0): return None;
        # Values
        val1 = 0 if not l1 else l1.val;
        val2 = 0 if not l2 else l2.val;
        # Sum
        summ = val1 + val2 + carry;
        value = summ % 10;
        carry = summ // 10;
        # Asigning Val to ListNode
        result = ListNode(value);
        # Next Pointer
        l1 = None if not l1 else l1.next;
        l2 = None if not l2 else l2.next;
        # Recursion
        result.next = self.addTwoNumbers(l1, l2, carry);
        # Return when hitting base case
        return result;
    
if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)));
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    res = Solution().addTwoNumbers(l1, l2);
    print(res);