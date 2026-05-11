class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ranger = len(nums)
        dissed = []
        nums_set = set(nums)
        for i in range(1, ranger+1):
            if i not in nums_set:
                dissed.append(i)

        return dissed
        