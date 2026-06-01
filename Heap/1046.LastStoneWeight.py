class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        rev_array = [-number for number in stones]
        
        heapq.heapify(rev_array)
        
        while len(rev_array) > 1:
            
            first = heapq.heappop(rev_array)
            second = heapq.heappop(rev_array)
            
            if first != second:
                heapq.heappush(rev_array,first - second)
                
        return rev_array[0] if rev_array else 0