class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_dict = {}
        for i in range(len(nums)):
            
            if nums[i]-1 in nums_dict:
                nums_dict[nums[i]] = nums_dict.pop(nums[i]-1) + 1

            elif nums[i]-1 not in nums_dict:
                nums_dict[nums[i]] = 1

        return max(nums_dict.values())
