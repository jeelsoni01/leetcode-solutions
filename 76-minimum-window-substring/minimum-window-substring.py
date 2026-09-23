class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for ch in t:
            count[ch] = count.get(ch, 0) + 1

        left = 0
        need = len(t)
        start = 0
        min_len = float("inf")

        for right in range(len(s)):
            if s[right] in count:
                if count[s[right]] > 0:
                    need -= 1
                count[s[right]] -= 1

            while need == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                if s[left] in count:
                    count[s[left]] += 1
                    if count[s[left]] > 0:
                        need += 1

                left += 1

        return "" if min_len == float("inf") else s[start:start + min_len]