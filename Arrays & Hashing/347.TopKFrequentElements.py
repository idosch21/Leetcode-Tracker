class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        numbers_freq = collections.Counter(nums)
        
        # Bucket sort: index = frequency, value = list of numbers with that freq
        # Max possible frequency = len(nums)
        freq_array = [[] for _ in range(len(nums) + 1)]
        
        for key, value in numbers_freq.items():
            # Place number in bucket corresponding to its frequency
            freq_array[value].append(key)
        
        # Collect results from highest frequency buckets first
        res = []
        for i in range(len(freq_array) - 1, 0, -1):
            for num in freq_array[i]:
                res.append(num)
                if len(res) == k:
                    return res

# TRICK: Bucket sort by frequency. Use frequency as index in array.
# Iterate from highest freq down, collect k elements.
# T(N) = O(n)
# S(N) = O(n)  