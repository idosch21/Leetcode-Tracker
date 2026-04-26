class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for i in range(len(gifts)):
            gifts[i] *= -1
        
        heapq.heapify(gifts)
        
        for i in range(k):
            max_val = -heapq.heappop(gifts)
            heapq.heappush(gifts,-math.isqrt(max_val))
            
        return -sum(gifts)