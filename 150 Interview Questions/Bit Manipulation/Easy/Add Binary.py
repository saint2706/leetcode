class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary_sum = lambda a, b: bin(int(a, 2) + int(b, 2))
        return binary_sum(a, b)[2:]
