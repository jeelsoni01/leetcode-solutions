class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        count = [0] * (len(nums) + 1)
        res = left = prefix = distinct = 0
        
        for right in range(len(nums)):
            if count[nums[right]] == 0:
                distinct += 1
            count[nums[right]] += 1
            
            if distinct > k:
                count[nums[left]] -= 1
                left += 1
                distinct -= 1
                prefix = 0
                
            while count[nums[left]] > 1:
                count[nums[left]] -= 1
                left += 1
                prefix += 1
                
            if distinct == k:
                res += prefix + 1
                
        return res