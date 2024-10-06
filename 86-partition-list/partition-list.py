# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:        
        lower_dummy = ListNode(0)
        higher_dummy = ListNode(0)
        lower_tail = lower_dummy
        higher_tail = higher_dummy

        current_node = head

        
        while current_node:
            if current_node.val < x:
                
                lower_tail.next = current_node
                lower_tail = current_node
            else:
                
                higher_tail.next = current_node
                higher_tail = current_node
            
            current_node = current_node.next
        
        
        higher_tail.next = None

        
        lower_tail.next = higher_dummy.next

        
        head = lower_dummy.next
        return head