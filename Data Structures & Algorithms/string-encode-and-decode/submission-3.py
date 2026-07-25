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
            j = i
            while j < len(s) and s[j] != '.':
                j += 1
            n = int(s[i:j])
            i = j + 1 # is is now just after '.'
            j = i + n
            got = s[i:j]
            res.append(got)
            i = j
        return res
