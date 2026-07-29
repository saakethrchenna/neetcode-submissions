class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comps = defaultdict(list)
        for i in strs:
            d = [0]*26
            for e in i:
                d[ord(e) - ord('a')] = d[ord(e) - ord('a')] + 1
            comps[tuple(d)].append(i)
        return list(comps.values())
            

        