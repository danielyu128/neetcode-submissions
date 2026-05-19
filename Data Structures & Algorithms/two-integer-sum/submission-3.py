class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            number_needed = target - nums[i]
            if number_needed in nums[i+1:]:
                j = nums.index(number_needed)
                return [i,j]
