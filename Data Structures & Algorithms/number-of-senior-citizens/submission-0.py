class Solution:
    def countSeniors(self, details: List[str]) -> int:
        number = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                number += 1
        return number


        