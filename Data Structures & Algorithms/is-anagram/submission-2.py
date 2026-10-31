class Solution:
    # hash table
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        counts_t = {}

        for c in s:
            counts_s[c] = counts_s.get(c, 0) + 1
        for c in t:
            counts_t[c] = counts_t.get(c, 0) + 1
        
        if counts_s == counts_t:
            return True
        else:
            return False

        