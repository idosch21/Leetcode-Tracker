class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        K Closest Points to Origin: Find the k points that are closest to (0, 0).
        
        TRICK USED:
        - Min-Heap: We use a min-heap to store tuples of (squared_distance, point). 
        - Squared Distance: To compare distances, we use x^2 + y^2 instead of sqrt(x^2 + y^2). This is more efficient and sufficient because the square root function is monotonic.
        - Two-Step Process: First, push every point into the heap to organize them by distance, then extract the k smallest.
        
        WHY IT WORKS:
        - A min-heap maintains the property that the smallest element (shortest distance) is always at the root.
        - By popping from the heap k times, we are guaranteed to retrieve the points in increasing order of their distance from the origin.
        """
        
        # Initialize the result list and an empty list for the heap
        result = []
        heap = []
        
        # Iterate through each coordinate point in the input
        for point in points:
            # Calculate squared Euclidean distance and push it with the point into the heap
            # heapq.heappush maintains the min-heap property based on the first element of the tuple
            heapq.heappush(heap, (point[0]**2 + point[1]**2, point))
            
        # Extract the k closest points by popping from the min-heap k times
        for _ in range(k):
            # Each pop returns the point with the current smallest distance
            result.append(heapq.heappop(heap)[1])
            
        return result 

# COMPLEXITY ANALYSIS:
# T(n) = O(N log N) - Time Complexity
#   - N is the total number of points.
#   - Pushing N elements into the heap takes O(N log N) time.
#   - Popping K elements takes O(K log N) time.
#
# S(n) = O(N) - Space Complexity
#   - The heap stores all N points from the input.
#   - The result list stores K points, but the primary memory driver is the heap.