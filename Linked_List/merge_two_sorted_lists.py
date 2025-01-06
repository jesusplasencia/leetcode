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
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if (not list1): return list2;
    #     if (not list2): return list1;
        
    #     val1 = 0 if not list1 else list1.val;
    #     val2 = 0 if not list2 else list2.val;
        
    #     result = ListNode();
    #     if (val1 < val2):
    #         result.val = val1;
    #         list1 = list1.next;
    #     else:
    #         result.val = val2;
    #         list2 = list2.next;
        
    #     result.next = self.mergeTwoLists(list1, list2);
    #     return result;

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0);
        current = dummy;

        while (list1 and list2):
            if (list1.val <= list2.val):
                current.next = ListNode(list1.val);
                list1 = list1.next;
            else:
                current.next = ListNode(list2.val);
                list2 = list2.next;
            current = current.next;
        current.next = list1 if list1 else list2;
        
        return dummy.next;

if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)));
    l2 = ListNode(1, ListNode(3, ListNode(4)));
    res = Solution().mergeTwoLists(l1, l2);
    print(res);