class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []
        if not nums:
            return 0
        
        for num in nums:
            heaq.heappush(heap,num)
            
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]