from typing import Optional;
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1): return list2;
        if (not list2): return list1;
        
        val1 = 0 if not list1 else list1.val;
        val2 = 0 if not list2 else list2.val;
        
        result = ListNode();
        if (val1 < val2):
            result.val = val1;
            list1 = list1.next;
        else:
            result.val = val2;
            list2 = list2.next;
        
        result.next = self.mergeTwoLists(list1, list2);
        return result;