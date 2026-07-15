class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        res = [0, 0]
        def check(l, r):
            nonlocal length, res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > length:
                    res = [l, r]
                    length = r - l
                l -= 1
                r += 1
        i = 0
        while i < len(s):
            check(i, i)
            check(i, i + 1)
            i += 1
        return s[res[0]:res[1]+1]