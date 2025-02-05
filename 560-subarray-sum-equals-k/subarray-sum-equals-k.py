class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        prefix_sums = {0:1}
        prefix_sum = 0
        # [1,4,3,5,2,3 ] , 6

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_sums:
                count += prefix_sums[prefix_sum - k]
            prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1
        return count

            
        