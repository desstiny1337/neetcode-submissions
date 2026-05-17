from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)

        answer = -1

        for num, count in freq.items():
            if num == count:
                answer = max(answer, num)

        return answer