class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        sorted_keys = sorted(counts, key=counts.get, reverse=True)
        print(sorted_keys)
        result = sorted_keys[:k]

        return result