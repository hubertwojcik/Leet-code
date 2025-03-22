class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {} # val -> index

        for index,num in enumerate(nums):
            if target - num in hash:
                return [index, hash[ target - num]]
            hash[num] = index
        