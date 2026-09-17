class Solution:
    def reversePairs(self, nums):
        def merge_sort(arr):
            if len(arr) <= 1:
                return 0

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            count = merge_sort(left) + merge_sort(right)

            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j

            arr[:] = sorted(left + right)

            return count

        return merge_sort(nums)