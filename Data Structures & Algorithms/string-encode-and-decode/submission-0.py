class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for s in strs:
            cnt = str(len(s))
            out += cnt
            out += '.'
            out += s
        print(out)
        return out

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            dot = s.index('.')
            n = int(s[:dot])
            s = s[dot+1:] # skip the dot
            got = s[:n]
            s = s[n:]
            res.append(got)
        return res
