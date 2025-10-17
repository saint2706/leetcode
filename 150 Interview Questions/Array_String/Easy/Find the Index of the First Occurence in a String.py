class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1

        # Build prefix (failure) table for the needle using the KMP preprocessing step.
        prefix = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = prefix[j - 1]
            if needle[i] == needle[j]:
                j += 1
                prefix[i] = j

        # Scan the haystack using the prefix table to find the first occurrence.
        j = 0
        for i, char in enumerate(haystack):
            while j > 0 and char != needle[j]:
                j = prefix[j - 1]
            if char == needle[j]:
                j += 1
                if j == len(needle):
                    return i - len(needle) + 1

        return -1
