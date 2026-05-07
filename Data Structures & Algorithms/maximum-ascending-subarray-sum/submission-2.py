class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i = 1
        sums = []
        sums.append(nums[0])
        sum = nums[i - 1]
        for num in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                sum += nums[i]
            elif nums[i] <= nums[i-1]:
                sum = nums[i]
            i+=1
            sums.append(sum)
        return max(sums)
        