class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        x2 = str(x)[::-1]
        # print(x1 == x2)
        return x1 == x2
