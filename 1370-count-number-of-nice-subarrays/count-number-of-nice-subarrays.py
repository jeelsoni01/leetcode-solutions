class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        res = left = count = odds = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odds += 1
                count = 0
                
            while odds == k:
                if nums[left] % 2 == 1:
                    odds -= 1
                count += 1
                left += 1
                
            res += count
            
        return res