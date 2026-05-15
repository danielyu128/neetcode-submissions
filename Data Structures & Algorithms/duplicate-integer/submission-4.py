class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        set_nums = set()

        for number in nums:
            if number not in set_nums:
                set_nums.add(number)
            else:
                return True
        return False