class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(i, current):
            if i == len(nums):
                result.append(current[:])
                return

            backtrack(i + 1, current)

            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

        backtrack(0, [])
        return result