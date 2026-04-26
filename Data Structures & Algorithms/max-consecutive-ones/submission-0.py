class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        seq_counter = 0
        max_counter = 0

        for num in nums:
            if num == 0:
                seq_counter = 0
            else:
                seq_counter += 1
                max_counter = max(max_counter, seq_counter)
        return max_counter

        