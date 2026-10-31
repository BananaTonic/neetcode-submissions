class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in dictionary:
                dictionary[sorted_s].append(s)
            else:
                dictionary[sorted_s] = [s]
        return list(dictionary.values())