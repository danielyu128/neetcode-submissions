class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        value_needed = {}

        for i in range(len(nums)):

            other_number_needed = target - nums[i]

            if other_number_needed in value_needed.values():
                return [nums.index(other_number_needed),i]
                
                
            else:
                value_needed[i] = nums[i]
