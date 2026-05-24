class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        
        for course, preq in prerequisites:
            adj_list[course].append(preq)
            
        visiting = set()
        visited = set()
        
        def dfs(course):
            
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            
            for preq in adj_list[course]:
                if not dfs(preq):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            
            return True
    
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True