
def dist(x, y):
    return x * x + y * y

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (dist(x, y), x, y))
        
        
        res = []
        for _ in range(k):
            if heap:
                _, x, y = heapq.heappop(heap)
                res.append([x, y])
        return res
        
