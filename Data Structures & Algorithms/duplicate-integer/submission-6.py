class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        list_of_nums = set()

        for num in nums:
            if num in list_of_nums:
                return True
            else:
                list_of_nums.add(num)