from typing import Optional;
# Definition for singly-linked list.
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
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: Optional[int] = 0) -> Optional[ListNode]:
    #     if (not l1 and not l2 and carry == 0): return None;
    #     # Values
    #     val1 = 0 if not l1 else l1.val;
    #     val2 = 0 if not l2 else l2.val;
    #     # Sum
    #     summ = val1 + val2 + carry;
    #     value = summ % 10;
    #     carry = summ // 10;
    #     # Asigning Val to ListNode
    #     result = ListNode(value);
    #     # Next Pointer
    #     l1 = None if not l1 else l1.next;
    #     l2 = None if not l2 else l2.next;
    #     # Recursion
    #     result.next = self.addTwoNumbers(l1, l2, carry);
    #     # Return when hitting base case
    #     return result;
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0);
        current = dummy;
        carry = 0;

        while (l1 or l2 or carry != 0):
            val1 = 0 if not l1 else l1.val;
            val2 = 0 if not l2 else l2.val;

            summ = val1 + val2 + carry;
            val = summ % 10;
            carry = summ // 10;
            
            current.next = ListNode(val);
            current = current.next;

            l1 = l1.next if l1 else None;
            l2 = l2.next if l2 else None;

        return dummy.next;

if __name__ == "__main__":
    l1 = ListNode(1, ListNode(8));
    l2 = ListNode(0)
    res = Solution().addTwoNumbers(l1, l2);
    print(res);