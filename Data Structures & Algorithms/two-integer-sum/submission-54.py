class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # maps number -> index

        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference], i]  # return both indices
            seen[num] = i  # store number and its index

        return []