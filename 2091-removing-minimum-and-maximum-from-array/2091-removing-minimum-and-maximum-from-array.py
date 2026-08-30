class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # Ensure min_index comes before max_index
        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # 1. Remove both from front
        option1 = right + 1

        # 2. Remove both from back
        option2 = len(nums) - left

        # 3. One from front and one from back
        option3 = (left + 1) + (len(nums) - right)

        return min(option1, option2, option3)