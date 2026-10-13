from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashD = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            hashD[key].append(word)
        return list(hashD.values())
        