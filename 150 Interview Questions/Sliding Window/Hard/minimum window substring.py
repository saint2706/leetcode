class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        left, right = 0, 0
        count = m
        min_window = ""

        while right < n:
            if s[right] in t_freq:
                if t_freq[s[right]] > 0:
                    count -= 1
                t_freq[s[right]] -= 1

            while count == 0:
                if not min_window or len(min_window) > right - left + 1:
                    min_window = s[left : right + 1]

                if s[left] in t_freq:
                    t_freq[s[left]] += 1
                    if t_freq[s[left]] > 0:
                        count += 1

                left += 1

            right += 1

        return min_window
