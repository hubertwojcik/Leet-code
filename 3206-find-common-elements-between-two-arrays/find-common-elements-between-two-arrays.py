class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result1, result2 = 0, 0

        for i in nums1:
            if i in nums2:
                result1 += 1
        
        for i in nums2:
            if i in nums1:
                result2 += 1
                     


        return [result1, result2]

        