class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python implements min heap, but we need max heap
        negstones = [-x for x in stones]
        heapq.heapify(negstones)

        while len(negstones) > 1:
            x = -heapq.heappop(negstones)
            y = -heapq.heappop(negstones)

            if x == y:
                continue
            if x > y:
                heapq.heappush(negstones, -(x - y))
            else:
                heapq.heappush(negstones, -(y - x))
        
        return 0 if not negstones else -negstones[0]

