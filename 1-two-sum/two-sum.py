class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in mp:
                return [mp[diff], i]

            mp[num] = i