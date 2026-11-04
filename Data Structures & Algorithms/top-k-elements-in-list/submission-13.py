class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        sorted_pairs = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        return [pair[0] for pair in sorted_pairs[:k]]