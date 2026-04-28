class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#I want to bucket sort the numbers based on their freq in nums
#it means that I will have at most len(nums) buckets.
#for each number in a freq I will put it in an array called freq_array
#and then go over the array from the end and "pop" out k numbers

        numbers_freq = collections.Counter(nums)
        freq_array = [[] for _ in range(size +1)]
        res = []

        
        for key,value in enumerate(numbers_freq):
            freq_array[value].append(key)
            #creates the array with the value(freq) as the index and inside the correct number it represents
            
        for i in range(len(freq_array)-1,0,-1):
            for num in freq_array[i]:
                res.append(num)
                if len(res)== k:
                    return res  