class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        my_set = set(nums)
        max_seq = 0
        
        for number in my_set:
            if number -1 not in my_set:
                current = number
                counter = 1
                while current + 1 in my_set:
                    counter += 1
                    current += 1
                max_seq = max(max_seq,counter)
        return max_seq