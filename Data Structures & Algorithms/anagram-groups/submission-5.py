class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for i in strs:
            k = "".join(sorted(i))
            if k not in h:
                h[k] = [i]
            else:
                h[k].append(i)
        return list(h.values())


