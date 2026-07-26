class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for c in tasks:
            counts[ord(c)-ord('A')] += 1
        counts.sort()

        idleSlots = (counts[-1] - 1) * n
        for i in range(24, -1, -1):
            idleSlots -= min(counts[i], counts[-1] - 1)
        

        if idleSlots >= 0:
            return idleSlots + len(tasks)
        else:
            return len(tasks)
