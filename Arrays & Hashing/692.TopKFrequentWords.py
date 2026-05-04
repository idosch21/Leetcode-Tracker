class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = Counter(words)
        result = []
        
        bucket = [[] for _ in range(len(words)+1)]
        
        for key,value in freq.items():
            bucket[value].append(key)
            
        for i in range(len(words)-1,-1,-1):
            if bucket[i]:
                bucket[i].sort()
            for word in bucket[i]:
                result.append(word)
                if len(result) == k:
                    return result
                