class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_elements = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in list_elements:
                return [list_elements.get(difference),i]
            list_elements[nums[i]] = i