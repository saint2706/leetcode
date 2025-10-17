class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # Shift the accumulated result left, append the current least significant bit
            result <<= 1
            result |= n & 1
            n >>= 1
        return result
