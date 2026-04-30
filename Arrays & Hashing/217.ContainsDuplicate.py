class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Build a set from nums - duplicates automatically removed
        new_set = set(nums)
        
        # If set size != array size, duplicates existed
        return len(new_set) != len(nums)

# TRICK: Set automatically removes duplicates. Compare set size vs array size.
# T(N) = O(n)
# S(N) = O(n)