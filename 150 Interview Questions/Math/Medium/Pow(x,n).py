class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            return x**n
        elif n == 0:
            return 1
        elif n < 0:
            y = 1 / x
            n = -1 * n
            return y**n
