class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # empty set for indexes

        for i, num in enumerate(nums): # for loop through list nums
            difference = target - num
            if difference in seen:
                return [seen[difference], i]
            seen[num] = i
        return []
