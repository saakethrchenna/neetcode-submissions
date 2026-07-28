class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        vals = {}
        valt = {}
        for i in s:
            if i in vals:
                vals[i] = vals[i] + 1
            else:
                vals[i] = 1
        for e in t:
            if e in valt:
                valt[e] = valt[e] + 1
            else:
                valt[e] = 1
        return valt == vals
        
        