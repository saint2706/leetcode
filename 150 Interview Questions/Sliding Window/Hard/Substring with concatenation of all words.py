class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n = len(s)
        word_len = len(words[0])
        total_len = len(words) * word_len
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        result = []
        for i in range(n - total_len + 1):
            window = s[i : i + total_len]
            freq = {}
            for j in range(0, total_len, word_len):
                word = window[j : j + word_len]
                if word not in word_freq:
                    break
                freq[word] = freq.get(word, 0) + 1
                if freq[word] > word_freq.get(word, 0):
                    break
            else:
                result.append(i)

        return result
