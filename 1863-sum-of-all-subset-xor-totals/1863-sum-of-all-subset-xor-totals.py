class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        result = 0

        for num in nums:
            result |= num

        return result * (1 << (len(nums) - 1))