
def dist(x, y):
    return x * x + y * y

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-dist(x, y), x, y))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []
        for _, x, y in heap:
            res.append([x, y])
        return res
        
