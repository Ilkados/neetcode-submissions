
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Prev_map = {} # val : index
        for i , n in enumerate(nums):
            diff = target - n

            if diff in Prev_map:
                return [Prev_map[diff],i]
            Prev_map[n] = i