class MedianFinder:

    def __init__(self):
        self.max_heap = [] # left
        self.min_heap = [] # right
    
    def __balance(self):
        while len(self.min_heap) + 1 > len(self.max_heap):
            mn = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, mn)

        while len(self.max_heap) > len(self.min_heap):
            mx = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, mx)
        

    def addNum(self, num: int) -> None:
        if not self.min_heap: heapq.heappush(self.min_heap, num); self.__balance(); return
        if not self.max_heap: heapq.heappush_max(self.max_heap, num); self.__balance(); return

        top = self.min_heap[0]
        if num < top: heapq.heappush(self.min_heap, num)
        else: heapq.heappush_max(self.max_heap, num)

        self.__balance()

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + self.max_heap[0]) / 2.0
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return self.max_heap[0]
        