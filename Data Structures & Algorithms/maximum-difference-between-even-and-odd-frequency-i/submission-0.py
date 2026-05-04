class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        even = []
        odd = []
        for value in cnt.values():
            if value % 2 == 0:
                even.append(value)
            else:
                odd.append(value)
        return max(odd) - min(even)
        