class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = defaultdict(list)
        
        for source,dest,time in times:
            adj_list[source].append([dest,time])
            
        heap = []
        heapq.heappush(heap,(0,k))
        visited = set()
        max_time = 0
        
        while heap:
            current_time , node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            max_time = current_time
            
            for neighboor in adj_list[node]:
                if neighboor[0] not in visited:
                    heapq.heappush(heap,(current_time + neighboor[1],neighboor[0]))
        if len(visited) != n:
            return -1
        return max_time