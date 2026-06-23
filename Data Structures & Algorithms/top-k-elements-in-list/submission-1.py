class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can also do heapify - need to build (freq, val) tuple first to push in the min-heap

        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        heap = []

        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
