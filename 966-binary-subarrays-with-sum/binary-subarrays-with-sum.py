class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = {0: 1}
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num

            if prefix - goal in count:
                ans += count[prefix - goal]

            count[prefix] = count.get(prefix, 0) + 1

        return ans