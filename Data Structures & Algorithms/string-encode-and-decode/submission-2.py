class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            cnt = str(len(s))
            result.append(cnt)
            result.append('.')
            result.append(s)
        return ''.join(result)

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
