class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)

        right_max = -1
        for i in range(length -1, -1,-1):
            new_max=max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr






        