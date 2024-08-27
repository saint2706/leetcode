class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        i = 0
        n = len(s)

        while i < n:
            if i + 1 < n and symbol_values[s[i]] < symbol_values[s[i + 1]]:
                total += symbol_values[s[i + 1]] - symbol_values[s[i]]
                i += 2
            else:
                total += symbol_values[s[i]]
                i += 1

        return total
