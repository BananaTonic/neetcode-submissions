class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cdic = {}
        prev = 0
        seq_counter = 0

        for i, c in enumerate(s):
            if c in cdic:
                prev = max(prev, cdic[c] + 1)

            cdic[c] = i
            seq_counter = max(seq_counter, i - prev + 1)

        return seq_counter
