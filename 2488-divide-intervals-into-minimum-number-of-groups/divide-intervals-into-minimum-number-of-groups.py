class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        starts = sorted(l for l, r in intervals)
        ends = sorted(r for l, r in intervals)

        i = j = 0
        groups = 0
        max_groups = 0

        while i < len(intervals):
            if starts[i] <= ends[j]:
                groups += 1
                max_groups = max(max_groups, groups)
                i += 1
            else:
                groups -= 1
                j += 1

        return max_groups