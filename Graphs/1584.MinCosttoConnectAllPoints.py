class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        #fisrt solution distance array P(n^2)
        n = len(points)
        connected = set()
        dist_array = [float('inf')]*n
        dist_array[0] = 0
        total_cost = 0
        
        while len(connected) < n:
            
            current_node = -1
            current_weight = float('inf')
            
            for i in range(n):
                if i not in connected and dist_array[i] < current_weight:
                    current_node = i
                    current_weight = dist_array[i]
                    
            connected.add(current_node)
            total_cost += current_weight
            
            for i in range(n):
                if i not in connected:
                    x1,y1 = points[current_node]
                    x2,y2 = points[i]
                    
                    dist = abs(x1-x2)+abs(y1-y2)
                    if dist < dist_array[i]:
                        dist_array[i] = dist
                        
        return total_cost
    """
    #second solution min heap O(n^2Logn)
    
        visited = set()
        heap = [(0,0)]
        total_cost = 0
        
        while heap:
            cost, current_node = heapq.heappop(heap)
            
            if current_node in visited:
                continue
            visited.add(current_node)
            total_cost += cost
            
            if len(visited) == len(points):
                break
            
            for neighboor in range(len(points)):
                if neighboor not in visited:
                    x1,y1 = points[current_node]
                    x2,y2 = points[neighboor]
                    
                    dist = abs(x1-x2)+abs(y1-y2)
                    
                    heapq.heappush(heap,(dist,neighboor))
        return total_cost
        """