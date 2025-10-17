class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)

        # Count how many papers have a given citation count, capping the bucket at n.
        buckets = [0] * (n + 1)
        for citation in citations:
            buckets[min(citation, n)] += 1

        papers = 0
        for h in range(n, -1, -1):
            papers += buckets[h]
            if papers >= h:
                return h

        return 0
