class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Return the sum of two binary strings without using base conversions."""

        i, j = len(a) - 1, len(b) - 1
        carry = 0
        bits = []

        # Walk both strings from right to left, adding corresponding bits and carry.
        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += ord(a[i]) - ord("0")
                i -= 1

            if j >= 0:
                total += ord(b[j]) - ord("0")
                j -= 1

            bits.append(str(total & 1))
            carry = total >> 1

        # The bits were collected from least significant to most significant.
        return "".join(reversed(bits))
