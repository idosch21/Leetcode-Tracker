class Solution:
    def edgeScore(self, edges: List[int]) -> int:

        scores = [0]*len(edges)
        max_val = float('-inf')
        min_index = 0
        
        for key,value in enumerate(edges):
            scores[value] += key
        
        for index,value in enumerate(scores):
            if value > max_val:
                max_val = value
                min_index = index
        return min_index