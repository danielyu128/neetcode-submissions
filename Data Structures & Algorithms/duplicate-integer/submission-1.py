class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        times_appeared = {}
        for num in nums:
            if num in  times_appeared:
                times_appeared[num] = times_appeared[num] + 1
            elif num not in times_appeared:
                times_appeared[num] = 1
        
        for value in times_appeared.values():
            if value > 1:
                return True
        return False