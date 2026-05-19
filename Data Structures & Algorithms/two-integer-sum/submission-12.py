class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        opposite = {}

        for num in nums:
            needed = target - num
            if num in opposite:
                return [num,needed]
            opposite[num]=needed
    