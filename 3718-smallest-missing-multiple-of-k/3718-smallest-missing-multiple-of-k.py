class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = k
        while n in nums:
            n += k
        return n