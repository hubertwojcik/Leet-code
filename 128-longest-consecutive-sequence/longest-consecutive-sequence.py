class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:  
            if num - 1 not in num_set: 
                length = 1
                while num + 1 in num_set:
                    num += 1
                    length += 1
                longest = max(longest, length)

        return longest