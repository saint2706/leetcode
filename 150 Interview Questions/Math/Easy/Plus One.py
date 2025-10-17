class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1

        for idx in range(len(digits) - 1, -1, -1):
            total = digits[idx] + carry
            digits[idx] = total % 10
            carry = total // 10

            if carry == 0:
                break

        if carry:
            digits.insert(0, carry)

        return digits
