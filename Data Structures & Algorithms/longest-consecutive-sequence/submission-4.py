class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_dict = {}
        for i in range(len(nums)):
            
            if nums[i]-1 or nums[i]+1 in nums_dict:

                if nums[i]-1:
                    nums_dict[nums[i]] = nums_dict.pop(nums[i]-1) + 1
                    nums_dict[nums[i-1]] = nums_dict[nums[i]]

                elif nums[i]+1:
                    nums_dict[nums[i]] = nums_dict.pop(nums[i]+1) + 1
                    nums_dict[nums[i+1]] = nums_dict[nums[i]]


            elif nums[i]-1 or nums[i]+1 not in nums_dict and nums:
                nums_dict[nums[i]] = 1


        print(nums_dict.values())
        return max(nums_dict.values())
