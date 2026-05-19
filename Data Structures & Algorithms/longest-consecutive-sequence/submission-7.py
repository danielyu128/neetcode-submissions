class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_dict = {}
        start = nums[0]
        while start in nums:
            if nums[0] - 1 not in nums:
                if nums[0] + 1 in nums:
                    nums_dict[nums[0] + 1] += 1
                    nums.remove(nums[0])
            
        return max(nums_dict.values())