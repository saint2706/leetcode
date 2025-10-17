from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        res = 1
        m = len(points)
        for i in range(m):
            slopes = defaultdict(lambda: 1)
            x1, y1 = points[i]
            for j in range(i + 1, m):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx == 0:
                    key = (1, 0)
                else:
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g
                    if dx < 0:
                        dx *= -1
                        dy *= -1
                    key = (dy, dx)

                slopes[key] += 1
                res = max(res, slopes[key])
        return res
