# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        dummy_node = ListNode(0)
        dummy_node.next = head
        prev_node = dummy_node

        while prev_node.next is not None and prev_node.next.next is not None:
            current_node = prev_node.next
            next_node = current_node.next

            prev_node.next = next_node
            current_node.next = next_node.next
            next_node.next = current_node

            prev_node = current_node
        
        return dummy_node.next