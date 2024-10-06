# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        numbers = []
        current = head
        
        while current:
            numbers.append(current.val)
            current=current.next
        reversed_array = numbers[::-1]

        num = 0 

        for index,val in enumerate(reversed_array):
            num+=val* pow(2,index)
            
        return num