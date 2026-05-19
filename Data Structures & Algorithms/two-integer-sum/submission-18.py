class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        opposite = {}

        for num in nums:
            needed = target - num
            if needed in opposite:
                return [num,opposite[needed]]
            opposite[num]=needed
    