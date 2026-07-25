class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums) # k, v (count)
        minHeap = []
        for num, count in freqs.items():
            heapq.heappush(minHeap, (count, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        
        return [v for _, v in minHeap]