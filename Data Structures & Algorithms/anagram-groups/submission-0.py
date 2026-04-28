class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        used = []
        for s in strs:
            if s in used:
                continue
            group=[]
            for word in strs:
                if sorted(word) == sorted(s):
                    group.append(word)
                    used.append(word)
            result.append(group)

        return result

        