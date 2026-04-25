class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alr_used = set(nums)
        if len(alr_used) == len(nums):
            return False
        return True
        