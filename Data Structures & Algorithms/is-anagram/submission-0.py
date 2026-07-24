class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        v1 = [0] * 256
        v2 = [0] * 256
        for c in s:
            v1[ord(c)] += 1
        for c in t:
            v2[ord(c)] += 1
        for i in range(len(v1)):
            if v1[i] != v2[i]:
                return False
        return True