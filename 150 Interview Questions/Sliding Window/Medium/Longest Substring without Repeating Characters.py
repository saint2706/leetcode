class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        last_seen = {}
        max_len = 0

        while right < n:
            current_char = s[right]
            if current_char in last_seen:
                left = max(left, last_seen[current_char] + 1)

            last_seen[current_char] = right
            right += 1
            max_len = max(max_len, right - left)

        return max_len
