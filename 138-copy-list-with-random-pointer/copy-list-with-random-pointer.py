"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_nodes = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            old_nodes[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy_node = old_nodes[curr]
            copy_node.next = old_nodes[curr.next]
            copy_node.random = old_nodes[curr.random]
            curr = curr.next
        
        return old_nodes[head]