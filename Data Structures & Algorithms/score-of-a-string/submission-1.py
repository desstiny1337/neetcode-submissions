class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(1, len(s)):
            current = s[i]
            previous = s[i-1]

            sum += abs(ord(current) - ord(previous))
        return sum

        