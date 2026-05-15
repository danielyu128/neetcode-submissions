class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        single_elements = set()
        for num in nums:
            if num in single_elements:
                return True
            single_elements.add(num)
        return False