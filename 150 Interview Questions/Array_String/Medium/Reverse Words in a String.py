class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into a list of words
        words = s.split()

        # Reverse the list of words
        words.reverse()
        # Alternatively: words = words[::-1]

        # Join the words with a single space character
        return " ".join(words)
