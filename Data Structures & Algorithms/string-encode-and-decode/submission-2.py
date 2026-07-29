class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in strs:
            out = out + str(len(i)) + "$" + i
        return out


    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            val = ""
            e = i
            while s[e] != "$":
                val += s[e]
                e += 1
            size = len(val)
            val = int(val)
            string = s[e+1:e+val+1]
            out.append(string)
            i += val + size + 1
        return out 
            