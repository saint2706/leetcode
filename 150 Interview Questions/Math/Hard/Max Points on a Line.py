from math import gcd


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        res = 1
        m = len(points)
        for i in range(m):
            d = {}
            [x1, y1] = points[i]
            for j in range(i + 1, m):
                [x2, y2] = points[j]
                key = ""
                if x1 == x2:
                    key = "0"
                    d[key] = d.get(key, 1) + 1
                else:
                    sig = ""
                    y = y2 - y1

                    x = x2 - x1
                    if x * y < 0:
                        sig = "-"
                    x = abs(x)
                    y = abs(y)
                    p = gcd(x, y)
                    key = sig + str(y // p) + "_" + str(x // p)
                    d[key] = d.get(key, 1) + 1
                res = max(res, d[key])
        return res
