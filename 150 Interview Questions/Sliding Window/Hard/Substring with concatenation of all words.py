class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        n = len(s)
        word_len = len(words[0])
        total_len = len(words) * word_len
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        result = []
        for offset in range(word_len):
            left = offset
            seen = {}
            matches = 0

            for right in range(offset, n - word_len + 1, word_len):
                word = s[right : right + word_len]

                if word in word_freq:
                    seen[word] = seen.get(word, 0) + 1
                    matches += 1

                    while seen[word] > word_freq[word]:
                        left_word = s[left : left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        matches -= 1

                    if matches == len(words):
                        result.append(left)
                        left_word = s[left : left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        matches -= 1
                else:
                    seen.clear()
                    matches = 0
                    left = right + word_len

        return result
