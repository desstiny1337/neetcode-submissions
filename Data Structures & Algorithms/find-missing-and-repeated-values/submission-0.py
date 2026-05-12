class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        grid_len = len(grid)
        repeated_values = []
        for i in grid:
            for j in i:
                repeated_values.append(j)

        seen = set()
        repeated = 0

        for i in repeated_values:
            if i in seen:
                repeated = i
            else:
                seen.add(i)

        missing = 0
        for i in range(1, grid_len*grid_len+1):
            if i not in repeated_values:
                missing = i
                break
        return [repeated, missing]

        