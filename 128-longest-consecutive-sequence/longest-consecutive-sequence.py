class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_values= set(nums)
        longest=0

        for num in nums:
            if (num-1) not in unique_values:
                length=0
                while(num+length) in unique_values:
                    length+=1
                longest = max(length,longest)
        return longest
            
            
        


        