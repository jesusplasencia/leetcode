from typing import Optional;
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head: return None;
        
        curr = head;
        old_to_new = {};
        
        while (curr):
            node = Node(x=curr.val)
            old_to_new[curr] = node;
            curr = curr.next;
            
        curr = head;
        while (curr):
            new_node = old_to_new[curr];
            new_node.next = old_to_new[curr.next] if curr.next else None;
            new_node.random = old_to_new[curr.random] if curr.random else None;
            curr = curr.next;
            
        return old_to_new[head];

if __name__ == "__main__":
    sol = Solution();
    Head = Node(7, Node(13, Node(11, Node(10, Node(1)))));
    C = sol.copyRandomList(Head);
    while (C):
        print(C.val);
        C = C.next;