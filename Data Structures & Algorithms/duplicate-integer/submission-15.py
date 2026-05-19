class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            current_element = nums[i]
            if current_element in seen:
                return True
            seen.add(current_element)
        
        return False