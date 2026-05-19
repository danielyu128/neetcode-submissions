class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        single_elements = {}
        for num in nums:
            if num in single_elements:
                return True
            single_elements.add(num)
        return False