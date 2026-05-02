class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)

        for i in range(n):
            c1 = s[i]
            c2 = t[i]
            for j in range(n):
                if s[j] == c1 and t[j] != c2:
                    return False
                if t[j] == c2 and s[j] != c1:
                    return False
        return True

        