class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers starting from the end of each array
        end1 = m - 1        # Last valid element in nums1
        end2 = n - 1        # Last element in nums2
        end_all = m + n - 1 # Last position in the merged nums1
        
        # Merge from the end (right to left) to avoid overwriting nums1 elements
        # This works because nums1 has extra space at the end
        while end2 >= 0:
            if end1 >= 0 and nums1[end1] > nums2[end2]:
                # nums1's element is larger - place it at the end
                nums1[end_all] = nums1[end1]
                end1 -= 1
            else:
                # nums2's element is larger or nums1 is exhausted
                nums1[end_all] = nums2[end2]
                end2 -= 1
            end_all -= 1

# T(n) = O(m + n) - single pass through all elements
# S(n) = O(1) - only using pointer variables, no extra space
            
        