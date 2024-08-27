class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)
        for i in range(n):
            if citations[i] < i + 1:
                return i
        return n
