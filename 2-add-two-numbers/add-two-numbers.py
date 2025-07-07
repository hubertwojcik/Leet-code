# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        carry = 0 
        while l1 or l2 or carry:
            val_first = l1.val if l1 else 0
            val_second = l2.val if l2 else 0

            val = val_first + val_second + carry
            carry = val // 10
            value = val % 10
            current.next = ListNode(value)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next