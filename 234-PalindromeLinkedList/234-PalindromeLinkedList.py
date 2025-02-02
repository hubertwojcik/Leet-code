# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        values = []
        temp = head

        while temp is not None:
            values.append(temp.val)
            temp = temp.next

        begin_index, last_index = 0, len(values) -1

        while begin_index < last_index:
            if values[begin_index] != values[last_index]:
                return False
            begin_index += 1
            last_index -= 1
        
        return True
        