class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count = {}
        left = 0
        
        for right, fruit in enumerate(fruits):
            # Add the current fruit to the basket
            count[fruit] = count.get(fruit, 0) + 1
            
            # If we have more than 2 types of fruit, shift the window
            if len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
                
        # The maximum size of the window is the length of the array minus the left pointer
        return right - left + 1