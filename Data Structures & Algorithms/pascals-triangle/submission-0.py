class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        result = []
        for i in range(numRows):
            result.append(row)
            row = [sum(x) for x in zip([0]+row, row+[0])]

        return result


        