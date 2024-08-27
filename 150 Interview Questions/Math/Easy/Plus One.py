class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join(list(map(str, digits))))
        num += 1
        num2 = []
        for i in range(len(str(num))):
            num2.append(num % 10)
            num //= 10
        return num2[::-1]
