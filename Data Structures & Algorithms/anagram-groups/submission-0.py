class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list) # keyd by list as well
        for s in strs:
            fingerprint = [0] * 26
            for c in s:
                fingerprint[ord(c)-ord('a')] += 1
            out[tuple(fingerprint)].append(s)
        res = []
        for v in out.values():
            res.append(v)
        return res
