class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        my_hash = {0:1}
        
        counter = 0
        current_sum = 0
        
        for number in nums:
            current_sum += number
            
            if current_sum - k in my_hash:
                counter += my_hash[current_sum - k]
            my_hash[current_sum] = my_hash.get(current_sum,0) + 1
        return counter