class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows
        i = 0
        direction = 1

        for c in s:
            rows[i] += c
            if i == 0:
                direction = 1
            elif i == numRows - 1:
                direction = -1
            i += direction

        return "".join(rows)
