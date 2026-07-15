class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        anchor = 0
        total = 0
        i = 0
        subc = 0
        if len(s) < 2:
            return len(s)
        while i < len(s):
            if s[i]  in window:
                anchor = max(window[s[i]], anchor)
                subc = 0
            subc += 1
            window[s[i]] = i
            curr = i - anchor
            total = max(total, curr, subc)
            i += 1
        return total
        