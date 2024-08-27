class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i = 0

        while i < len(words):
            # Calculate the number of words to fit in the current line
            j = i + 1
            line_len = len(words[i])
            while j < len(words) and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            # Calculate the number of spaces to insert between words
            num_words = j - i
            num_spaces = maxWidth - line_len
            if num_words == 1 or j == len(words):
                # Left justify the text
                spaces_between = 1
                extra_spaces = 0
            else:
                spaces_between = num_spaces // (num_words - 1)
                extra_spaces = num_spaces % (num_words - 1)

            # Construct the line
            line = words[i]
            for k in range(i + 1, j):
                if extra_spaces > 0:
                    line += " " * (spaces_between + 1)
                    extra_spaces -= 1
                else:
                    line += " " * spaces_between
                line += words[k]

            # Pad the remaining space on the right
            line += " " * (maxWidth - len(line))

            result.append(line)
            i = j

        return result
