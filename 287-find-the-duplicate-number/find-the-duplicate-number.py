class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = {}

        for i in nums:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        
        for key in lookup:
            if lookup[key] > 1:
                return key