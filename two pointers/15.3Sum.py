class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #2sum2 in a for loop , if i have a,b,c where a+b = -c 
        #-c is the target and a b are the values from 2sumII that i found.


        start=0
        end = len(nums)-1
        ans = []

        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            start = i+1
            end = len(nums)-1
            while (start<end):
                total = nums[start]+nums[end]+nums[i]
                if total > 0:
                    end-=1
                elif total < 0:
                    start+=1
                else:
                    ans.append([nums[start],nums[end],nums[i]])
                    start+=1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
            
            
        return ans

            
