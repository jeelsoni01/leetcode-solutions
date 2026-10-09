class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atMost(target: int) -> int:
            if target < 0: return 0
            
            res = left = 0
            for right in range(len(nums)):
                # Subtract 1 if the number is odd (num % 2 == 1), 0 if even
                target -= nums[right] % 2
                
                # Shrink window until we have at most 'target' odd numbers again
                while target < 0:
                    target += nums[left] % 2
                    left += 1
                    
                # Add the number of valid subarrays ending at the right pointer
                res += right - left + 1
                
            return res

        return atMost(k) - atMost(k - 1)