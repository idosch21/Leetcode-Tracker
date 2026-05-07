class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count frequency of each word
        freq = collections.Counter(words)
        result = []
        
        # Create buckets where index is the frequency
        bucket = [[] for _ in range(len(words) + 1)]
        
        # Place words into buckets based on their frequency count
        for key, value in freq.items():
            bucket[value].append(key)
            
        # Iterate from highest frequency bucket down to lowest
        for i in range(len(words), -1, -1):
            if bucket[i]:
                # Sort words in the same bucket lexicographically
                bucket[i].sort()
                for word in bucket[i]:
                    result.append(word)
                    # Return once k words are collected
                    if len(result) == k:
                        return result

# TRICK: Use Bucket Sort (index = frequency) and sort each bucket to handle lexicographical order.
# T(N) = O(N log N) in the worst case (if many unique words have the same frequency)
# S(N) = O(N)