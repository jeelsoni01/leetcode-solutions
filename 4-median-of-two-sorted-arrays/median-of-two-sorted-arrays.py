class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = half - i

            a_left = nums1[i - 1] if i > 0 else float("-inf")
            a_right = nums1[i] if i < m else float("inf")
            b_left = nums2[j - 1] if j > 0 else float("-inf")
            b_right = nums2[j] if j < n else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if (m + n) % 2:
                    return float(max(a_left, b_left))

                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            if a_left > b_right:
                right = i - 1
            else:
                left = i + 1