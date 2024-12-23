from collections import deque;

q = deque();
print(q); # deque([])

q.append(5);
q.append(6);

# popleft
print(q.popleft()); # 5

# peek from left side - O(1)
print(q[0]);

# peek from right side - O(1)
print(q[-1]);